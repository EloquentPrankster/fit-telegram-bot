from pyrogram import Client

from config import BOT_TOKEN, API_HASH, API_ID

app = Client("My", api_id=int(API_ID),
             api_hash=API_HASH, bot_token=BOT_TOKEN)
