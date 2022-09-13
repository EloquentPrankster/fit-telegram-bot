from aiogram import types
from bot import disp
from db_api.get.get_timetable_db import get_timetable_db
@disp.message_handler(commands=['gettt'])
async def get_timetable(message:types.Message):
    await message.answer(get_timetable_db())
