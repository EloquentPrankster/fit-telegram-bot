from email import message
import sys
import psycopg2
from psycopg2 import Error
from config import *

try:
    db = psycopg2.connect(DB_URI,
                          sslmode='require')
    db_cursor = db.cursor()
except (Exception, Error) as error:
    print("Ошибка при работе с БД")
    sys.exit(f'{error}')
