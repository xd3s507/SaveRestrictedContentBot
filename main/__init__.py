#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("21037154", default=None, cast=int)
API_HASH = config("b70bf9ef5b87f66bdbd39968daf33dcf", default=None)
BOT_TOKEN = config("6500428452:AAETFvY6cUKoze_qMf34C_xzJ5QhnPRQudo", default=None)
SESSION = config("6500428452", default=None)
FORCESUB = config("Save_alshehri_bot", default=None)
AUTH = config("xn_ik", default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("Save_alshehri_bot", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
