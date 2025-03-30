# code by Asad Ali Owner Off Jankari Ki Duniya Youtube Channel


import os
import sys
import asyncio
from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message
from config import bot, call_py, HNDLR, contact_filter
from time import time
from datetime import datetime

# System Uptime
START_TIME = datetime.utcnow()
TIME_DURATION_UNITS = (
    ("Week", 60 * 60 * 24 * 7),
    ("Day", 60 * 60 * 24),
    ("Hour", 60 * 60),
    ("Min", 60),
    ("Sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(contact_filter & filters.command(["ping"], prefixes=f"{HNDLR}"))
async def ping(client, m: Message):
    start = time()
    current_time = datetime.utcnow()
    m_reply = await m.reply_text("`...`")
    delta_ping = time() - start
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await m_reply.edit(f"`{delta_ping * 1000:.3f} ms` \n**ᴜᴘᴛɪᴍᴇ 🇨🇳** - `{uptime}`")


@Client.on_message(contact_filter & filters.command(["restart"], prefixes=f"{HNDLR}"))
async def restart(client, m: Message):
    await m.reply("`Restarting...`")
    os.execl(sys.executable, sys.executable, *sys.argv)
    # You probably don't need it but whatever
    quit()


@Client.on_message(contact_filter & filters.command(["help"], prefixes=f"{HNDLR}"))
async def help(client, m: Message):
    HELP = f"**🇨🇳 ʜᴇʟᴘ ᴍᴇɴᴜ 🇨🇳** \n\n**sᴇᴍᴜᴀɴʏᴀ ʙɪsᴀ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ɪɴɪ**\n**ᴍᴇᴍᴜʟᴀɪ ᴍᴜsɪᴄ** {HNDLR}play\n** ᴜɴᴛᴜᴋ ᴍᴇᴍᴜᴛᴀʀ ᴠɪᴅᴇᴏ (ᴊᴀɴɢᴀɴ ʙᴏᴋᴇᴘ ᴛᴏʟᴏʟ)** {HNDLR}vplay\n**ᴜɴᴛᴜᴋ ᴍᴇɴᴅᴇɴɢᴀʀᴋᴀɴ ʀᴀᴅɪᴏ** {HNDLR}stream (**ʟɪɴᴋ ʀᴀᴅɪᴏ**) \n**ᴜɴᴛᴜᴋ ʟɪᴠᴇsᴛʀᴇᴀᴍ** {HNDLR}vstream (ғᴏʀ .m3u8 / ʟɪᴠᴇ ʟɪɴᴋs) \n\n**ᴜɴᴛᴜᴋ sᴜᴅᴏ** (**ᴋᴀᴍᴜ ʙɪsᴀ ɢᴜɴᴀɪɴ ɪɴɪ ᴋᴀʟᴏ ᴋᴀᴍᴜ ᴅɪʙᴇʀɪᴋᴀɴ ᴀᴋsᴇs ᴏʟᴇʜ** @itsmeaeron **ᴀɢᴀʀ ᴅɪʙᴇʀɪᴋᴀɴ ᴀᴋsᴇs sᴜᴅᴏ**): \n**ᴍᴇʟɪʜᴀᴛ ᴘɪɴɢ ʙᴏᴛ** {HNDLR}ping \n**ᴍᴇʟᴇᴡᴀᴛɪ ᴘᴜᴛᴀʀᴀɴ** {HNDLR}skip \n**ᴍᴇɴᴊᴇᴅᴀ ᴘᴜᴛᴀʀᴀɴ** {HNDLR}pause ᴀɴᴅ **ᴍᴇʟᴀɴᴊᴜᴛᴋᴀɴ ᴘᴜᴛᴀʀᴀɴ ʏᴀɴɢ ᴅɪᴊᴇᴅᴀ **{HNDLR}resume \n**ᴍᴇɴsᴛᴏᴘ ᴘᴜᴛᴀʀᴀɴ** {HNDLR}stop / **ᴍᴇɴɢᴀᴋʜɪʀɪ ᴘᴜᴛᴀʀᴀɴ** {HNDLR}end \n**ʜᴇʟᴘ ᴍᴇɴᴜ** {HNDLR}help \n**ʀᴇsᴛᴀʀᴛ ʙᴏᴛ** {HNDLR}restart"
    await m.reply(HELP)


@Client.on_message(contact_filter & filters.command(["repo"], prefixes=f"{HNDLR}"))
async def repo(client, m: Message):
    REPO = f"**🇨🇳 ᴋᴀʟᴏ ᴋᴀᴍᴜ ᴍᴀᴜ ʀᴇᴘᴏ 🇨🇳** \n\n**ʙɪsᴀ ᴍᴇɴɢʜᴜʙᴜɴɢɪ** [ᴏɴᴡᴇʀ](t.me/itsmearion)\n**ᴋᴀʟᴏ ᴋᴀᴍᴜ sᴜᴋᴀ ᴘʀᴏᴊᴇᴄᴛ ᴀᴋᴜ, ᴛᴏʟᴏɴɢ ʙᴇʀɪᴋᴀɴ ʀᴇᴀᴄᴛ ᴅᴀɴ ᴊᴏɪɴ** [sᴜᴋᴀ](t.me/itsmeerickkkkkk) [ᴜᴘᴅᴀᴛᴇs](t.me/arionsupport) [ᴊᴏɪɴ](https://t.me/+BE4Cav641LdkYTRl)"
    await m.reply(REPO)
