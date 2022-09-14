from bot import disp
from aiogram import types

from db_api.get.get_access_db import get_access_db

@disp.message_handler(commands=['getacc'])
async def get_access(message: types.Message):
    list_of_access = get_access_db()
    pretty_list ='Список супер-пользователей:\n'
    if(len(list_of_access)==0):
        pretty_list+='пусто'
        return await message.answer(pretty_list)
    for i in list_of_access:
        pretty_list+=i+'\n'
    await message.answer(pretty_list)