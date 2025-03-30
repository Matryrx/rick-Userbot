import os
from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls

# For Local Deploy
if os.path.exists(".env"):
    load_dotenv(".env")

# Necessary Vars
API_ID = int(os.getenv("API_ID", "27917752"))
API_HASH = os.getenv("API_HASH", "bf6436f671e5363ed68edc1bb293d6d3")
SESSION = os.getenv("BQFTOGgATO0IiBHjH7NQAYnnskjqaA3iDtHQBL7ltPGmSYNiTvwWHcT8W5fijyr1EHVsUSQAztdcwfhzeL22nErljG7gIxcLRM-xLUa_uNrTVNulkcQX9pzuZ-F7DWgOs04A8WVikP4s_3p84kDT4bcieF6_D6U3XNqfTN8-V4PliX_Erlmej9FDp0jGAs7RRJwL2j0cOHKkBGlQ2L1HIA30zGfgz5iYs8_91UlIyMqkbcy3SbgYiQhl0sIQGECyNYTHYGqKbnmTNkN4o-j6BJHXGNJUtkQXjnaDYMxP1My1j1JAdFbs8tDb46Um8gzSXEHPemCD_X5nyUrGGebd0P8e1e6gAAAAGBhJzGAA")
HNDLR = os.getenv(".", "/")
GROUP_MODE = os.getenv("True", "True")


contact_filter = filters.create(
    lambda _, __, message: (message.from_user and message.from_user.is_contact)
    or message.outgoing
)


if GROUP_MODE == ("True" or "true"):
    grp = True
else:
    grp = False

GRPPLAY = grp
bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="AsadAlexaVCBot"))
call_py = PyTgCalls(bot)
