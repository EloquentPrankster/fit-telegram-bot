from bot import bot
from config import CHAT_TO_NOTIFY
from db_api.get.get_reminder_db import get_reminders_db
from handlers.reminder.helpers.show_reminders import show_reminders
async def notifier():
    list_of_reminders=get_reminders_db()
    if len(list_of_reminders) == 0: return
    await bot.send_message(chat_id=CHAT_TO_NOTIFY,text=show_reminders(list_of_reminders))