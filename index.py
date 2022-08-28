from init_handlers import init_handlers
from bot import disp
from aiogram import executor

if __name__ == '__main__':
    init_handlers()
    executor.start_polling(disp, skip_updates=True)
