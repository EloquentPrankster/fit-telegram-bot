from daemons.telegram.input_telegram import input_telegram
from main import module
import config


def init_telegram():

    module.bot = telebot.TeleBot(config.getCell('telegram_token'))
    print("Successfully loginned in telegram!")
    input_telegram()
