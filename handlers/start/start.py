from bot import disp
from aiogram import types


@disp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Бот FIT manager - задумка, реализованная для того, чтобы автоматизировать часть студенческой рутины"+
     ", такой как поиск расписания пар, получение списка группы, генерация очередей на пару, напоминание о событиях. "+
     "Все функции можно узнать введя команду /help. "+
     "Так же этот бот очень старается пересылать новости из ВК в телеграм.")
