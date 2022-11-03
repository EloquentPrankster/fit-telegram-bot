from bot import disp
from aiogram import types


@disp.message_handler(commands=["maxim"])
async def shiman_worktime(message: types.Message):
    await message.answer("Максим Матарас иди нахуй")
