from bot import disp
from aiogram import types
from utils.get_group_db import get_group_db
from utils.show_group import show_group


@disp.message_handler(commands=['getsub1'])
async def get_sub_1(message: types.Message):
    list = get_group_db(1)
    await message.answer(show_group(list))
