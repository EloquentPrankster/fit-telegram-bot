from aiogram import executor
from bot import bot


def main(disp):
    executor.start_polling(disp, skip_updates=True)
