from bot import disp
from aiogram import types
from utils.get_group_db import get_group_db
from utils.show_group import show_group


@disp.message_handler(commands=['getsub2'])
async def get_sub_2(message: types.Message):
    list =await get_group_db(2)
    await message.answer(show_group(list))
