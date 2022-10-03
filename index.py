import asyncio
from init_handlers import init_handlers
from bot import disp
from aiogram import executor
from db_api.core.db import *
from sheduler.core.core import sheduler
from aiogram import types
async def on_startup(_):
    await disp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустить бота"),
            types.BotCommand("help", "Вывести справку"),
            types.BotCommand("cancel", "Отмена команды"),
            types.BotCommand("getgroup", "Список группы"),
            types.BotCommand("getsub1", "Список подгруппы 1"),
            types.BotCommand("getsub2", "Список подгруппы 2"),
            types.BotCommand("setgroup", "Записать список группы"),
            types.BotCommand("getq1", "Очередь 1пг"),
            types.BotCommand("getq2", "Очередь 2пг"),
            types.BotCommand("setq", "Сгенерировать очередь"),
            types.BotCommand("getmind", "Список напоминаний"),
            types.BotCommand("setmind", "Установить напоминание"),
            types.BotCommand("remmind", "Удалить напоминание"),
            types.BotCommand("getacc", "Список админов"),
            types.BotCommand("setacc", "Дать админку"),
            types.BotCommand("remacc", "Забрать админку"),
            types.BotCommand("getshiman", "Расписание деканата"),
            types.BotCommand("setshiman", "Переписать расписание деканата"),
            types.BotCommand("gett", "Расписание занятий"),
            types.BotCommand("sett", "Установить ссылку на расписание"),
            types.BotCommand("getmesvk", "Получить сообщения из ВК"),
        ]
    )
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
