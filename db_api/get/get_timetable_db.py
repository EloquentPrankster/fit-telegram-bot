from db import db_cursor
def get_timetable_db()->str:
    """Returns url of timetable"""
    db_cursor.execute('select * from timetable')
    return db_cursor.fetchall()[0][0]