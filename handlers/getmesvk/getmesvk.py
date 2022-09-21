from aiogram import types
from bot import disp

from VK_api.transfer_messages.transfer_messages import transfer_messages

@disp.message_handler(commands=['getmesvk'])
async def getmesvk(message: types.Message):
    await transfer_messages()
