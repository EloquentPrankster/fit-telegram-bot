from bot import disp
from aiogram import types

from db_api.get_access_db import get_access_db
from db_api.set_access_db import set_access_db

@disp.message_handler(commands=['setacc'])
async def set_access(message: types.Message):
    usernames = message.text.replace(' ','').split('@')[1:]
    if len(usernames) ==0: return await message.answer("Укажите пользователей через @")
    users_from_db = get_access_db()
    for i in usernames:
        if i in users_from_db: 
            await message.answer(f'Пользователь {i} уже в базе')
            continue
        else:
            await message.answer(set_access_db(i))