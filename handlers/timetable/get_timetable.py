from aiogram import types
from bot import disp,bot

@disp.message_handler(commands=['gettt'])
async def get_timetable(message:types.Message):
    pass
