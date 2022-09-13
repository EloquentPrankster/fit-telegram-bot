import asyncio
from init_handlers import init_handlers
from bot import disp
from aiogram import executor
from db import *
from sheduler.core.core import sheduler

async def on_startup(_):
    asyncio.create_task(sheduler())

async def on_shutdown(_):
    db_cursor.close()
    db.close()
    print('Свет гаснет... Я... умираю...')

if __name__ == '__main__':
    init_handlers()
    executor.start_polling(
        disp, 
        skip_updates=True, 
        on_startup=on_startup, 
        on_shutdown=on_shutdown
        )
