from db import db_cursor
def get_reminders_db():
    db_cursor.execute('select * from reminder')
    return db_cursor.fetchall()