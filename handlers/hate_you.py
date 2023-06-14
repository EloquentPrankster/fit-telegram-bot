import logging
import random
from aiogram import types
import services


async def hate_you(message: types.Message):
    students = services.db_manager.get_students()
    rand = random.randint(0, len(students)-1)
    student_to_hate = f"{students[rand].name} {students[rand].patronymic}"
    list_of_things = [
        "иди нахуй", "лох", "отчисляется",
        "лицо нетрадиционной ориентации", "– ты норм", "покоритель негров",
        "любит негров", "ебет чурок", "ненавидит негров",
        "любит Калтыгина", "не сдаст Смелова",
        "сегодня моет парашу", f"го по пиву с {student_to_hate}",
        f"идет на свидание с {student_to_hate}",
        "едет на свидание с Кореньковой"
    ]
    rand = random.randint(0, len(students)-1)
    student_to_hate = f"{students[rand].name} {students[rand].patronymic}"
    await message.answer(f"{student_to_hate} {list_of_things[random.randint(0, len(list_of_things)-1)]}")
    logging.info(f"hate_you completed")
