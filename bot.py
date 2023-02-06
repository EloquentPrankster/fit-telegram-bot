import logging
from aiogram import Dispatcher,  Bot
from config import *
from aiogram.contrib.fsm_storage.memory import MemoryStorage

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
disp = Dispatcher(bot, storage=MemoryStorage())
