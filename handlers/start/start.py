from bot import disp
from aiogram import types


@disp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Привет, я FIT manager. Вот у меня будет куча функций, но я вам их не покажу)")
