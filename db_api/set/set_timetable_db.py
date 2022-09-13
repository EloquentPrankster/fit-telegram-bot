from db import db_cursor, db

def set_timetable_db(url:str)->bool:
    """
    Returns True if data has been added and False if not
    """
    try:
        db_cursor.execute('truncate timetable')
        db_cursor.execute(f"insert into timetable values ('{url}')")
        db.commit()
        return True
    except Exception as ex:
        db.rollback()
        print(ex)
        return False