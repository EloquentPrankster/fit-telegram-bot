from aiogram import executor
from bot import FitBot
if __name__ == "__main__":
    bot = FitBot()
    executor.start_polling(
        bot.dispatcher,
        skip_updates=True,
        on_startup=bot.on_startup,
        on_shutdown=bot.on_shutdown,
    )
