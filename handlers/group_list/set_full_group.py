from aiogram import types
from aiogram.dispatcher.filters import Command
from bot import disp
from handlers.group_list.states.OverwritingList import OverwritingList
from aiogram.dispatcher import FSMContext
from db_api.core.db import db_cursor, db
from db_api.get.get_group_db import get_group_db
import re

from handlers.rights.helpers.check_acc import has_access


@disp.message_handler(Command('setgroup'), state=None)
async def start_set(message: types.Message, state: FSMContext):
    if not has_access(message.from_user.username): return await message.answer("У вас нет прав на эту команду")
    old_list = await get_group_db()
    await state.update_data(Oldlist=old_list)
    split_list = ''
    for i in old_list:
        split_list += f'{i[1]}-{i[2]}\n'
    await message.answer(split_list)
    await message.answer("Это текущий список.\nСкопируйте, поправьте и отправьте новое. Проверьте правильность.\n Разделитель '-' обязателен!")
    await OverwritingList.Q1.set()


@disp.message_handler(state=OverwritingList.Q1)
async def stop_set(message: types.Message, state: FSMContext):
    new_list = message.text.split('\n')
    split_list = []
    for i in new_list:
        x = re.match(r'.* .* .*-[1|2]$', i)
        if x is None:
            return await message.answer('Каждая строка должна соответствовать шаблону "Ф И О-1|2".\n Скопируйте и вставьте список снова.')
        i = i.split('-')
        split_list.append(i[0])
        split_list.append(i[1])
    await message.answer('Идет обновление...')
    i = 0
    try:
        db_cursor.execute('TRUNCATE students')
    except Exception:
        db.rollback()
        await message.answer('Ошибка обновления таблицы. Проверьте корректность данных. Ну или админ падарас')
        return
    id = 1
    while i < len(split_list):
        try:
            db_cursor.execute(
                f"Insert into students (id,fio, subgroup) values (%s,%s,%s)", (id, split_list[i], split_list[i+1]))
            id += 1
        except (Exception):
            db.rollback()
            await message.answer('Ошибка обновления таблицы. Проверьте корректность данных. Ну или админ падарас')
            return
        i += 2
    db.commit()
    await message.answer('Список обновлен')
    await state.finish()
