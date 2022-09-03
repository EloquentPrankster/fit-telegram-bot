from db import db, db_cursor


def set_shiman_wt_db(old_wt: str, new_wt: str) -> bool:
    try:
        db_cursor.execute(
            f"UPDATE shiman SET worktime='{new_wt}' WHERE worktime='{old_wt}'")
        db.commit()
        return True
    except Exception as ex:
        db.rollback()
        print(ex)
        return False
