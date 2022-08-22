import psycopg2
from config import DB_URI

db = psycopg2.connect(DB_URI, sslmode='require')
db_cursor = db.cursor()
