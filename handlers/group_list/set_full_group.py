from aiogram import types
from aiogram.dispatcher.filters import Command
from bot import disp
from handlers.group_list.states.OverwritingList import OverwritingList
from aiogram.dispatcher import FSMContext
from db import db_cursor, db
from utils.get_group_db import get_group_db
import re


@disp.message_handler(Command('setgroup'), state=None)
async def start_set(message: types.Message, state: FSMContext):
    old_list = get_group_db()
    await state.update_data(Oldlist=old_list)
    splitlist = ''
    for i in old_list:
        splitlist += f'{i[1]}-{i[2]}\n'
    await message.answer(splitlist)
    await message.answer("Это текущий список.\nСкопируйте, поправьте и отправьте новое. Проверьте правильность.\n Разделитель '-' обязателен!")
    await OverwritingList.Q1.set()


@disp.message_handler(state=OverwritingList.Q1)
async def stop_set(message: types.Message, state: FSMContext):
    new_list = message.text.split('\n')
    splist = []
    for i in new_list:
        x = re.match(r'.* .* .*-[1|2]$', i)
        if x is None:
            await message.answer('Каждая строка должна соответствовать шаблону ".* .* .*-[1|2]$".\n Скопируйте и вставьте список снова.')
            return
        i = i.split('-')
        splist.append(i[0])
        splist.append(i[1])
    await message.answer('Идет обновление...')
    i = 0
    try:
        db_cursor.execute('TRUNCATE students')
    except (Exception):
        db.rollback()
        await message.answer('Ошибка обновления таблицы. Проверьте корректность данных. Ну или админ падарас')
        return
    while i < len(splist):
        try:
            db_cursor.execute(
                f"Insert into students (fio, subgroup) values (%s,%s)", (splist[i], splist[i+1]))
        except (Exception):
            db.rollback()
            await message.answer('Ошибка обновления таблицы. Проверьте корректность данных. Ну или админ падарас')
            return
        i += 2
    db.commit()
    await message.answer('Список обновлен')
    await state.finish()
