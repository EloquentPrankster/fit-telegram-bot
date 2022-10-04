from aiogram import Dispatcher,  Bot
from config import *
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(token=API_TOKEN)
disp = Dispatcher(bot, storage=MemoryStorage())