from bot import disp
from aiogram import types
from db_api.get_group_db import get_group_db
from db_api.helpers.show_group import show_group


@disp.message_handler(commands=['getsub1'])
async def get_sub_1(message: types.Message):
    list = await get_group_db(1)
    await message.answer(show_group(list))
