import psycopg2
from psycopg2 import Error
from config import DB_URI
from bot import bot
try:
    db = psycopg2.connect(DB_URI, sslmode='require')
except (Exception, Error) as error:
    bot.send_message("Ошибка при работе с БД")
    bot.stop_poll()

db_cursor = db.cursor()
