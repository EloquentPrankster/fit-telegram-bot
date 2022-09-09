from db import db_cursor, db

def set_access_db(name:str):
    """Returns string with success or fault"""
    try:
        db_cursor.execute(f"insert into admins values ('{name}')")
        db.commit()
        return f"Пользователь {name} успешно добавлен"
    except Exception as ex:
        db.rollback()
        print(ex)
        return f"Ошибка добавления пользователя {name}"