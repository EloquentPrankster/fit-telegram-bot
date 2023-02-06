from bot import disp
from aiogram import types
from config import DEFAULT_ADMIN

from db_api.get.get_access_db import get_access_db
from db_api.set.set_access_db import set_access_db
from handlers.rights.helpers.check_acc import has_access


@disp.message_handler(commands=['setacc'])
async def set_access(message: types.Message):
    users_from_db = get_access_db()
    if len(users_from_db) == 0: set_access_db(DEFAULT_ADMIN)
    if not has_access(message.from_user.username): return await message.answer("У вас нет прав на эту команду")
    usernames = message.text.replace(' ', '').split('@')[1:]
    if len(usernames) == 0: return await message.answer("Укажите пользователей через @")
    for i in usernames:
        if i in users_from_db:
            await message.answer(f'Пользователь {i} уже в базе')
            continue
        else:
            await message.answer(set_access_db(i))
