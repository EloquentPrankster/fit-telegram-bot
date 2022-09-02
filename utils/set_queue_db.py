from db import db_cursor


def get_queue_db(subgroup: int = 0) -> list[tuple]:  # 0 = full group
    db_cursor.execute("INSERT INTO queues VALUES ()")
