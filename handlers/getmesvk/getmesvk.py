from aiogram import types
from bot import disp

from VK_api.get_messages.get_messages import get_messages

@disp.message_handler(commands=['getmesvk'])
async def getmesvk(message: types.Message):
    await get_messages()
