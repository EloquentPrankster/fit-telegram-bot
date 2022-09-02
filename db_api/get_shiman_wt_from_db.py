from db import db_cursor


def get_shiman_wt_from_db():
    db_cursor.execute("SELECT * FROM shiman")
    return db_cursor.fetchone()[0]
