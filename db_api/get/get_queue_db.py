from db_api.core.db import db_cursor


async def get_queue_db(subgroup: int):  # 0 = full group
    db_cursor.execute(
        f"SELECT * FROM queue WHERE subgroup='{subgroup}' order by position asc", )
    return db_cursor.fetchall()
