import os
from dotenv import load_dotenv
load_dotenv('./env/.env')
API_TOKEN = os.getenv('API_TOKEN')
DB_URI = os.getenv('DB_URI')
DB_NAME = os.getenv('DB_NAME')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
HOST = os.getenv('HOST')
