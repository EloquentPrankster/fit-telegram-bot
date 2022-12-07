import random
from bot import disp
from aiogram import types
from db_api.get.get_group_db import get_group_db


@disp.message_handler(commands=['exclude'])
async def exclude(message: types.Message):
    students_list = await get_group_db()
    student: str = ''
    while True:
        student = get_rand_student(students_list)
        if student != 'Позняк Полина Павловна':
            break
    await message.answer(f'Студент, которого завтра отчислят: {student}')


def get_rand_student(students_list):
    randint = random.randint(0, len(students_list)-1)
    return students_list[randint][1]
