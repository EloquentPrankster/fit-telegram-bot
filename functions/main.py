from aiogram import executor


def main(disp):
    executor.start_polling(disp, skip_updates=True)
