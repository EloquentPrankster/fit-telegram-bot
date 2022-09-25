from aiogram import types
from bot import disp,bot
from db_api.get.get_timetable_db import get_timetable_db
@disp.message_handler(commands=['gett'])
async def get_timetable(message:types.Message):
    await bot.send_document(message.chat.id,get_timetable_db())
