from bot import disp
from aiogram import types


@disp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Hello, I'm a bot")
