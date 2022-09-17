from bot import disp
from aiogram import types


@disp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Привет, я FIT manager. У меня тут куча функций\nПишите /help, чтобы узнать о них")
