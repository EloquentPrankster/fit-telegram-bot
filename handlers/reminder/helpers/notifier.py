from bot import bot
from db_api.get.get_reminder_db import get_reminders_db
from handlers.reminder.helpers.show_reminders import show_reminders
async def notifier():
    await bot.send_message(chat_id=1311967831,text=show_reminders(get_reminders_db()))