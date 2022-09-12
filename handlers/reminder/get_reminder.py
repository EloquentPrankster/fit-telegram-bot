from bot import disp
from aiogram import types
from db_api.get_reminders_db import get_reminders_db
from handlers.reminder.helpers.show_reminders import show_reminders

@disp.message_handler(commands=['getmind'])
async def get_reminder(message: types.Message):
    reminders= get_reminders_db()
    await message.answer(show_reminders(reminders))