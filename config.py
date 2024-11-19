import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", ""))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", ""))

# NAMA OWNER
OWNER = os.environ.get("OWNER", "Dᴇᴠᴇsʜ")

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", ""))

#Port
PORT = os.environ.get("PORT", "8030")

#Database
DB_URI = os.environ.get("DATABASE_URL", "")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", ""))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", ""))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "5"))

FILE_AUTO_DELETE = int(os.getenv("FILE_AUTO_DELETE", "600")) # auto delete in seconds

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>Hello, {first},!\n\nI’m your File Store Bot, \n\nThis bot is under @animehub_in 🍟</b>")
try:
    ADMINS=[5965340120]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b>⋄ 𝖢𝗁𝖺𝗇𝗇𝖾𝗅 𝖲𝗍𝖺𝗍𝗎𝗌 :-\n\n1. 𝖢𝗁𝖺𝗇𝗇𝖾𝗅 1 - ❌ 𝖭𝗈𝗍 𝖩𝗈𝗂𝗇𝖾𝖽\n2. 𝖢𝗁𝖺𝗇𝗇𝖾𝗅 2 - ❌ 𝖭𝗈𝗍 𝖩𝗈𝗂𝗇𝖾𝖽\n\n𝖧𝖾𝗒 {first}, 𝖯𝗅𝖾𝖺𝗌𝖾 𝖩𝗈𝗂𝗇 𝗆𝗒 𝖢𝗁𝖺𝗇𝗇𝖾𝗅𝗌 𝖺𝗇𝖽 𝗍𝗁𝖾𝗇 𝖼𝗅𝗂𝖼𝗄 𝗈𝗇 '↺𝖱𝖾𝖿𝗋𝖾𝗌h' 𝗍𝗈 𝗀𝖾𝗍 𝗒𝗈𝗎𝗋 𝖤𝗉𝗂𝗌𝗈𝖽𝖾(𝗌) ⤋</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "🚫 ᴏʜ ɴᴏ! ᴡʜᴇʀᴇ'ʀᴇ ʏᴏᴜʀ ʜᴀɴᴅs?!"

ADMINS.append(OWNER_ID)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   
