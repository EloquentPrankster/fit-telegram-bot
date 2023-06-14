import logging
import re
from aiogram import types
from aiogram.dispatcher import FSMContext
from config import CHAT_ID
from middlewares.check_admin import check_admin
from services import db_manager
from statemachine import StateMachine


async def get_group(message: types.Message):
    args = message.get_args()
    subgroup = None
    if len(args) != 0:
        if not re.match(r'^[1|2]$', args):
            return await message.reply("Параметр subgroup должен быть в диапазоне 1-2")
        subgroup = int(args[0])

    group_list = db_manager.get_students(subgroup)
    formatted_list = "".join(
        f"{x}. {i.surname} {i.name} {i.patronymic}\n" for x,i in enumerate(group_list,1))
    await message.answer(formatted_list if len(formatted_list)>0 else "Список пуст")
    logging.info(f"get_group completed")



async def set_group(message: types.Message):
    if not await check_admin(message.from_user.username,message.bot, CHAT_ID):
         return await message.answer("У вас нет прав на использование этой команды")
    group_list = db_manager.get_students()
    formatted_list = "".join(
        f"{i.patronymic}-{i.name}-{i.surname}-{i.subgroup}\n" for i in group_list)
    await message.reply(formatted_list if len(formatted_list)>0 else "Список пуст. \nВставьте свой в соответствии с паттерном \n[Фамилия]-[Имя]-[Отчество]-[1|2]")
    await message.answer("Скопируйте, исправьте и верните. Имейте ввиду, что при обновлении очереди сбиваются.\nИли используйте /cancel"if len(formatted_list)>0 else "Или используйте /cancel")
    await StateMachine.SET_GROUP.set()
    logging.info(f"set_group completed")

async def set_group2(message:types.Message, state:FSMContext):
    unformatted_list = message.text.split("\n")
    regex = r'^[А-я]*-[А-я]*-[А-я]*-[1|2]$'
    for i in unformatted_list:
        if re.match(regex,i) == None: 
            return await message.reply("Сообщение должно соответствовать паттерну:\n[Фамилия]-[Имя]-[Отчество]-[1|2].\nИсправьте или используйте /cancel")
    data = []
    for i in unformatted_list:
        (surname,name,patronymic,subgroup) = i.split('-')
        data.append((surname,name,patronymic,int(subgroup)))
    for i in data:
        print(i)
    result = db_manager.set_students(data)
    await state.finish()
    await message.answer("Список изменен" if result else "Произошла ошибка ;(")
    logging.info(f"set_group2 completed")
