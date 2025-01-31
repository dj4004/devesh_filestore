from bot import Bot
import pyrogram.utils
from pyrogram import utils as pyroutils

# pyrogram.utils.MIN_CHANNEL_ID = -1009147483647

pyroutils.MIN_CHAT_ID = -999999999999
pyroutils.MIN_CHANNEL_ID = -100999999999999

Bot().run()
