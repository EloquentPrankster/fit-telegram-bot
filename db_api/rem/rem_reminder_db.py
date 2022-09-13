from db import db_cursor,db
def rem_reminder_db(text_in_reminder:str, date_in_reminder:str)->bool:
    """
    Returns True if data has been deleted and False if not
    """
    try:
        db_cursor.execute(f"delete from reminder where date='{date_in_reminder}' and text='{text_in_reminder}'")
        db.commit()
        return True
    except Exception as ex:
        db.rollback()
        print(ex)
        return False