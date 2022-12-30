import re
from os import environ
from Script import script 

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '16225550'))
API_HASH = environ.get('API_HASH', '160343c3d2eaf54b556ad5a7c72a3b83')
BOT_TOKEN = environ.get('BOT_TOKEN', "5312771340:AAF3qvqPXHGwA02rYnpjHXuCVfyNU95N3m8")

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))

PICS = (environ.get('PICS', 'https://telegra.ph/file/0049172531be48c5f5b47.jpg https://telegra.ph/file/8ca3c51ec466715ee5381.jpg https://telegra.ph/file/51f1c14f4aadfd672247c.jpg https://telegra.ph/file/9866138ec0b12f9410925.jpg https://telegra.ph/file/ce07cc997cd42aa140d3b.jpg https://telegra.ph/file/d852c1fc90b34d308e280.jpg https://telegra.ph/file/f0d8eae5cd4ad05775d07.jpg https://telegra.ph/file/0b195dce66c2a315450f2.jpg https://telegra.ph/file/43b39c07c78cfd37a808a.jpg https://telegra.ph/file/7961814322398faa9825b.jpg https://telegra.ph/file/019e912c25fd0a63f0fb4.jpg https://telegra.ph/file/edc4f73fb01952262bbc7.jpg https://telegra.ph/file/812de3f7d6ee1dba8aae8.jpg https://telegra.ph/file/2befaf8ae38f1f13a863f.jpg https://telegra.ph/file/1c908c0d563fc59cfed59.jpg https://telegra.ph/file/af3d3dec56eec7eec877b.jpg https://telegra.ph/file/e10b0471ab32e9172b8e1.jpg https://telegra.ph/file/df79bdd0fc01923c75d53.jpg https://telegra.ph/file/d633f3eb86178c76b4344.jpg https://telegra.ph/file/2f6d52624c6524484d185.jpg https://telegra.ph/file/9e9f646ba67ea6e9821ba.jpg https://telegra.ph/file/8fd95166976a8d885eb5e.jpg https://telegra.ph/file/d7016ed0fe1844c9d01f9.jpg https://telegra.ph/file/14f2682a0a2f112fa0c78.jpg https://telegra.ph/file/c4bbccc5d5c6ee8e62c10.jpg https://telegra.ph/file/e66a664e211b4d8b8bbea.jpg https://telegra.ph/file/c402edf04e94e141e49f0.jpg https://telegra.ph/file/2bb3af487ad2660136411.jpg https://telegra.ph/file/593edafa458803059a9f3.jpg https://telegra.ph/file/66deac81536e35d020682.jpg')).split()
NOR_IMG = environ.get("NOR_IMG", "https://telegra.ph/file/f9a21dbe5d1dc30a12bc4.jpg")
MELCOW_VID = environ.get("MELCOW_VID", "https://telegra.ph/file/451f038b4e7c2ddd10dc0.mp4")
SPELL_IMG = environ.get("SPELL_IMG", "https://telegra.ph/file/5e2d4418525832bc9a1b9.jpg")

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1345179077').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001827951140').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '1345179077').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
support_chat_id = environ.get('-1001823409428')
reqst_channel = environ.get('-1001823409428')
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://pikachpatel:pikach432@pikachucluster.7cwyq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "pikachucluster")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Others
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]
MAX_B_TN = environ.get("MAX_B_TN", "5")
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/Movies4you_SP')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/Movies4youBackup')
MSG_ALRT = environ.get('MSG_ALRT', 'Wʜᴀᴛ Aʀᴇ Yᴏᴜ Lᴏᴏᴋɪɴɢ Aᴛ ?')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', -1001883857269))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'Movies4you_SP')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '-1001827951140')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
