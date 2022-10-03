import os
from dotenv import load_dotenv
load_dotenv('./env/.env')
API_TOKEN = os.getenv('API_TOKEN')
DB_URI = os.getenv('DB_URI')
CHAT_TO_NOTIFY = os.getenv('CHAT_TO_NOTIFY')
NEWS_CHAT = os.getenv('NEWS_CHAT')
DEFAULT_ADMIN = os.getenv('DEFAULT_ADMIN')
GROUP = os.getenv('GROUP')
VK_TOKEN = os.getenv('VK_TOKEN')
VK_PEER_ID = os.getenv('VK_PEER_ID')
