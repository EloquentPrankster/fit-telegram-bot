from datetime import  datetime
from db_api.rem.rem_reminder_db import rem_reminder_db


async def clean_reminder():
    x=datetime.now().date().strftime('%d-%m-%Y')
    rem_reminder_db(date_in_reminder=x, is_by_cleaner=True)
