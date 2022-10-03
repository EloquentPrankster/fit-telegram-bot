from db_api.core.db import db_cursor

def get_access_db()->list:
    """Get list of users with access to all commands"""
    db_cursor.execute('select admin from admins')
    a=[i[0] for i in db_cursor.fetchall()]
    return  a