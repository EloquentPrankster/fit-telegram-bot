from db_api.core.db import db_cursor, db

def set_reminder_db(date:str, text:str)->bool:
    """
    Returns True if data has been added and False if not
    """
    try:
        db_cursor.execute(f"insert into reminder (date, text) values (to_date('{date}', 'DD.MM.YYYY'), '{text}')")
        db.commit()
        return True
    except Exception as ex:
        db.rollback()
        print(ex)
        return False