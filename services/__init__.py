import logging
import models


class DatabaseManager:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(DatabaseManager, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.db = models.db

    def connect(self):
        self.db.connect(reuse_if_open=True)
        self.db.create_tables(models.MODELS)
        logging.info("DB Connected successful. Models updated.")
        return self

    def disconnect(self):
        self.db.close()
        logging.info("DB Closed successful")
        return self

    def get_students(self, subgroup: int | None = None) -> list[models.Student]:
        query = models.Student.select().order_by(models.Student.surname.asc())
        if subgroup is not None:
            query = query.where(models.Student.subgroup == subgroup)
        logging.info("get_students completed successful")
        return query

    def set_students(self, data: list[tuple]):
        with self.db.atomic() as transaction:
            try:
                models.Student.truncate_table()
                models.Student.insert_many(data, fields=[
                    models.Student.surname, models.Student.name, models.Student.patronymic, models.Student.subgroup]).execute()
                logging.info("set_students completed successful")
            except Exception as ex:
                transaction.rollback()
                logging.error(ex)
                return False
        return True

    def bind_username(self, username: str):
        with self.db.atomic() as transaction:
            try:
                models.Username(username=username).save()
                logging.info("bind_username completed successful")
            except Exception as ex:
                transaction.rollback()
                logging.error(ex)
                return False
        return True

    def unbind_username(self, username: str):
        res = models.Username.select().where(models.Username.username == username)
        if len(res) == 0:
            logging.info("unbind_username completed successful")
            return False
        with self.db.atomic() as transaction:
            try:
                models.Username.delete().where(models.Username.username == username).execute()
                logging.info("unbind_username completed successful")
            except Exception as ex:
                transaction.rollback()
                logging.error(ex)
                return False
        return True

    def get_bound_usernames(self) -> list[models.Student]:
        logging.info("get_bound_usernames completed successful")
        return models.Username.select()

    def get_descriptions(self) -> list[models.Description]:
        logging.info("get_descriptions completed successful")
        return models.Description.select()

    def add_description(self, data: str) -> bool:
        with self.db.atomic() as transaction:
            try:
                models.Description.insert(description=data).execute()
                logging.info("add_description completed successful")
            except Exception as ex:
                transaction.rollback()
                logging.error(ex)
                return False
        return True

    def del_description(self, id: str) -> bool:
        with self.db.atomic() as transaction:
            try:
                models.Description.delete().where(models.Description.id == id).execute()
                logging.info("del_description completed successful")
            except Exception as ex:
                transaction.rollback()
                logging.error(ex)
                return False
        return True

    def set_queue(self, queue: list, subgroup=None):
        query: list[models.Student] = models.Student.select()
        if subgroup is not None:
            query = query.where(models.Student.subgroup == subgroup)
            for x, i in enumerate(query):
                i.position_in_subgroup = queue[x]
            field = models.Student.position_in_subgroup
        else:
            for x, i in enumerate(query):
                i.position = queue[x]
            field = models.Student.position
        with self.db.atomic() as transaction:
            try:
                models.Student.bulk_update(
                    query, fields=[field])
                logging.info("set_queue completed successful")
            except Exception as ex:
                transaction.rollback()
                logging.error(ex)
                return False
        return True

    def get_queue(self, subgroup: int | None = None) -> list[models.Student]:
        query = models.Student.select()
        if subgroup is not None:
            query = query.where(models.Student.subgroup == subgroup)
            logging.info("get_queue completed successful")
            return query.order_by(models.Student.position_in_subgroup.asc())
        logging.info("get_queue completed successful")
        return query.order_by(models.Student.position.asc())


db_manager = DatabaseManager()
