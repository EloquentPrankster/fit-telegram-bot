from db import db_cursor


def get_queue_db(subgroup: int = 0):  # 0 = full group
    condition = f"WHERE subgroup={subgroup}" if subgroup > 0 else ""
    db_cursor.execute(f"SELECT * FROM queues {condition} order by fio asc")
    return db_cursor.fetchall()
