import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import BOT_TOKEN, NEWS_CHAT_ID, VK_PEER_ID, VK_TOKEN
from handlers import MESSAGE_HANDLERS
from services import db_manager
from tasks import TaskManager
import vk

logging.basicConfig(level=logging.INFO)


class FitBot:
    def __init__(self) -> None:
        self.bot = Bot(token=BOT_TOKEN)
        self.dispatcher = Dispatcher(self.bot, storage=MemoryStorage())
        self.task_manager = TaskManager()
        self.vk_manager = vk.VKManager(
            self.bot, VK_TOKEN, VK_PEER_ID, NEWS_CHAT_ID)

    async def on_startup(self, _):
        # set commands
        commands = []
        for handler in MESSAGE_HANDLERS:
            is_first_occurrence = True
            for func in handler["h"]:
                self.dispatcher.register_message_handler(
                    func["func"], commands=handler["c"] if is_first_occurrence else None, state=func['state'])
                is_first_occurrence = False
            commands.append(types.BotCommand(handler["c"], handler['d']))
        await self.dispatcher.bot.set_my_commands(commands)
        logging.info("Commands have been set up")
        try:
            db_manager.connect()
        except Exception as ex:
            logging.error(
                "Ошибка подключения к базе данных:\n" + ex)
            exit(1)
        # Start the task schedule asynchronously
        self.task_manager.schedule(self, db_manager)
        logging.info("Tasks have been scheduled")
        logging.info("Bot have been started")

    async def on_shutdown(self, _):
        db_manager.disconnect()
        logging.info("Бот успешно умер :/")
