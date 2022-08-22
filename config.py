import os
from dotenv import load_dotenv
load_dotenv('./env/.env')
API_TOKEN = os.getenv('API_TOKEN')
DB_URI = os.getenv('DB_URI')
