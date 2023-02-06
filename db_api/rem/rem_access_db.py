from db_api.core.db import db, db_cursor


def rem_access_db(name: str):
    """Returns string with success or fault"""
    try:
        db_cursor.execute(f"delete from admins where admin = '{name}'")
        db.commit()
        return f"Пользователь {name} успешно удален"
    except Exception as ex:
        db.rollback()
        print(ex)
        return f"Ошибка удаления пользователя {name}"
