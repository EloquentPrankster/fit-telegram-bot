from db_api.core.db import db_cursor, db
from handlers.queue.helpers.extract_fio_group import extract_fio_group


def set_queue_db(subgroup: int, list_of_students: list[tuple], list_of_positions: list[int]) -> bool:
    fios = extract_fio_group(list_of_students)
    try:
        db_cursor.execute(
            "delete from queue where subgroup = %s", str(subgroup))
        i = 0
        while i < len(list_of_students):
            db_cursor.execute(
                "insert into  queue (fio,subgroup, position) values (%s,%s,%s)",
                (fios[i], subgroup, str(list_of_positions[i]))
            )
            i += 1
        db.commit()
        return True
    except Exception as ex:
        db.rollback()
        print(ex)
        return False
