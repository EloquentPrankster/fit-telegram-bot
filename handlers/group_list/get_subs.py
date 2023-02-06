from bot import disp
from aiogram import types
from db_api.get.get_group_db import get_group_db
from handlers.group_list.helpers.show_group import show_group


@disp.message_handler(commands=['getsub1'])
async def get_sub_1(message: types.Message):
    await show_sub(1, message)


@disp.message_handler(commands=['getsub2'])
async def get_sub_2(message: types.Message):
    await show_sub(2, message)


async def show_sub(sub_num: int, message):
    list_of_students = await get_group_db(sub_num)
    await message.answer(show_group(list_of_students))
