from bot import disp
from aiogram import types
from db import db_cursor


@disp.message_handler(commands=['getgroup'])
async def get_group_list(message: types.Message):
    db_cursor.execute("SELECT * FROM students order by fio asc")
    list = db_cursor.fetchall()
    splitlist = ''
    splitlist += 'Список группы ИСИТ 3-1:\n'
    splitlist += '|№| ФИО |Подгруппа|\n'

    num = 1
    for student in list:
        splitlist += f'|{num}| {student[1]} |{student[2]}|\n'
        num += 1
    await message.answer(splitlist)
