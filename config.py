from os import getenv
from dotenv import load_dotenv
# env constants
load_dotenv('./env/.env')
# telegram
BOT_TOKEN = getenv("BOT_TOKEN")
CHAT_ID = getenv("CHAT_ID")
NEWS_CHAT_ID = getenv("NEWS_CHAT_ID")
# database
DATABASE_NAME = getenv("DATABASE_NAME")
DATABASE_USER = getenv('DATABASE_USER')
PASSWORD = getenv("PASSWORD")
HOST = getenv("HOST")
PORT = getenv("PORT")
# vk
VK_TOKEN = getenv("VK_TOKEN")
VK_PEER_ID = getenv("VK_PEER_ID")
