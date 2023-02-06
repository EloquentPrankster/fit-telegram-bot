from db_api.core.db import db_cursor


def get_access_db() -> list:
    """Get list of users with access to all commands"""
    db_cursor.execute('select admin from admins')
    list_of_admins = [i[0] for i in db_cursor.fetchall()]
    return list_of_admins
