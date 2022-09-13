from aiogram import types
from aiogram.dispatcher.filters import Command
from bot import disp
from db_api.set.set_reminder_db import set_reminder_db
from handlers.reminder.exceptions.InvalidDate import InvalidDate
from handlers.reminder.helpers.check_date import check_date
from handlers.reminder.helpers.check_reminder_regex import check_reminder_regex
from handlers.reminder.states.Reminder import Reminder
from handlers.rights.helpers.check_acc import has_access
from aiogram.dispatcher import FSMContext
@disp.message_handler(Command('setmind'), state=None)
async def set_mind(message: types.Message):
    if not has_access(message.from_user.username): return await message.answer("У вас нет прав на эту команду")
    await message.answer('Введите напоминание по шаблону \n"DD.MM.YYYY**Текст(не болee 400 символов)"')
    await Reminder.Q1.set()



@disp.message_handler(state=Reminder.Q1)
async def stop_set_mind(message: types.Message, state: FSMContext):
    message_text =message.text
    if check_reminder_regex(message_text) is None: return await message.answer('Строка должна соответствовать шаблону')
    arr=message_text.split('**')
    date, text=arr[0],arr[1]
    try:
        check_date(date)
    except InvalidDate as InvDate:
        return await message.answer(InvDate.text)
    await message.answer('Добавление данных...')
    await message.answer('Данные добавлены' if set_reminder_db(date,text) else 'Ошибка добавления, отмена команды')
    await state.finish()
