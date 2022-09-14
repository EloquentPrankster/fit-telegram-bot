from bot import bot
from config import CHAT_TO_NOTIFY
from db_api.get.get_reminder_db import get_reminders_db
from handlers.reminder.helpers.show_reminders import show_reminders
async def notifier():
    await bot.send_message(chat_id=CHAT_TO_NOTIFY,text=show_reminders(get_reminders_db()))