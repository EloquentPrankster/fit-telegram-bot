import re
from aiogram import types
from aiogram.dispatcher.filters import Command
from bot import disp
from db_api.rem.rem_reminder_db import rem_reminder_db
from handlers.reminder.states.Reminder import Reminder
from handlers.rights.helpers.check_acc import has_access
from db_api.get.get_reminder_db import get_reminders_db
from handlers.reminder.helpers.show_reminders import show_reminders
from aiogram.dispatcher import FSMContext

@disp.message_handler(Command('remmind'),state=None)
async def start_remove_reminder(message: types.Message):
    if not has_access(message.from_user.username): return await message.answer("У вас нет прав на эту команду")
    reminders= get_reminders_db()
    if len(reminders)==0: return await message.answer('Список напоминаний пуст!')
    await message.answer(show_reminders(reminders))
    await message.answer('Введите номер напоминания, которое надо удалить:')
    await Reminder.Z1.set()

@disp.message_handler(state=Reminder.Z1)
async def stop_remove_reminder(message: types.Message, state: FSMContext):
    text = message.text
    x = re.match('^[0-9]*$',text)
    if x is None: return await message.answer('Введите циферку, только циферку')
    position = int(text)
    list_of_reminders=get_reminders_db()
    if(len(list_of_reminders)<position): return await message.answer('Циферка больше, чем последняя циферка списка, введите ещё одну')
    reminder_to_remove = list_of_reminders[position-1]
    text_in_reminder, date_in_reminder=reminder_to_remove[0],reminder_to_remove[1]
    await message.answer('Данные удалены' if rem_reminder_db(text_in_reminder, date_in_reminder) else "Ошибка удаления, отмена команды")
    await state.finish()