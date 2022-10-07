from db_api.core.db import db_cursor,db
def rem_reminder_db(text_in_reminder:str='', date_in_reminder:str='', is_by_cleaner:bool =False)->bool:
    """
    Returns True if data has been deleted and False if not\n
    is_by_cleaner means that Reminders will be deleted if their date is less than today's date\n
    If is_by_cleaner specified then there is no need to specify text_in_reminder
    """
    if is_by_cleaner:
        try:
            db_cursor.execute(f"DELETE FROM reminder WHERE date < to_date('{date_in_reminder}', 'DD-MM-YYYY')")
            db.commit()
            return True
        except Exception as ex:
            db.rollback()
            print(ex)
            return False
    try:
        db_cursor.execute(f"delete from reminder where date='{date_in_reminder}' and text='{text_in_reminder}'")
        db.commit()
        return True
    except Exception as ex:
        db.rollback()
        print(ex)
        return False