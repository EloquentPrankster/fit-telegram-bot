from db import db_cursor


def get_group_db(subgroup=0):  # 0 = full group
    condition = f"WHERE subgroup={subgroup}" if subgroup > 0 else ""
    db_cursor.execute(f"SELECT * FROM students {condition} order by fio asc")
    return db_cursor.fetchall()
