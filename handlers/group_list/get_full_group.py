from bot import disp
from aiogram import types
from db_api.get.get_group_db import get_group_db
from handlers.group_list.helpers.show_group import show_group


@disp.message_handler(commands=['getgroup'])
async def get_full_group(message: types.Message):
    group_list = await get_group_db()
    await message.answer(show_group(group_list))
