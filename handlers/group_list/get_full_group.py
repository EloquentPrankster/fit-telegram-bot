from bot import disp
from aiogram import types
from utils.get_group_from_db.get_group_db import get_group_db
from utils.show_group_list.show_group import show_group


@disp.message_handler(commands=['getgroup'])
async def get_full_group(message: types.Message):
    list = get_group_db()
    await message.answer(show_group(list))
