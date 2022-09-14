from aiogram import types
from bot import disp
from db_api.set.set_timetable_db import set_timetable_db
from handlers.rights.helpers.check_acc import has_access

import re
@disp.message_handler(commands=['sett'])
async def get_timetable(message:types.Message):
    if not has_access(message.from_user.username): return await message.answer("У вас нет прав на эту команду")
    try:
        ref=message.text.split(' ',maxsplit=1)[1]
    except Exception:
        return await message.answer('Неправильный синтаксис команды')
    x=re.match(r'^https://it.belstu.by/wp-content/uploads.*\.pdf$',ref)
    if x is None: return await message.answer('Неправильная ссылка')
    await message.answer('Данные добавлены' if set_timetable_db(ref) else 'Ошибка добавления, отмена команды')