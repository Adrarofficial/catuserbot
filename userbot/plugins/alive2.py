"""Check if userbot alive or not . """


import asyncio , time
from telethon import events
from userbot import StartTime , catdef
from platform import uname
from userbot import CMD_HELP, ALIVE_NAME, catdef , catversion
from userbot.utils import admin_cmd,sudo_cmd
from telethon import version
from platform import python_version, uname

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "cat"
USERNAME = str(Config.LIVE_USERNAME) if Config.LIVE_USERNAME else "@Jisan7509"
CAT_IMG = Config.ALIVE_PIC

@borg.on(admin_cmd(outgoing=True, pattern="alive$"))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = alive.message
    uptime = await catdef.get_readable_time((time.time() - StartTime))
    if alive.reply_to_msg_id:
        reply_to_id = await alive.get_reply_message()
    if CAT_IMG:
          cat_caption  = f"🚴‍♂️**MY BOT IS RUNNING SUCCESFULLY**\n\n"
         cat_caption += f"**Database Status: Databases Functioning Normally!**\n"   
         cat_caption += f"⏳`Telethon Version:` **{version.__version__}**\n"
         cat_caption += f"⏳`Python Version:` **{python_version()}**\n"
         cat_caption += f"⏳`CatUserbot Version:` **{catversion}**\n"
         cat_caption += f"⏳`Cat Uptime:` **{uptime}**\n\n"         
         cat_caption += f"**Cat is Always With You, My Masters!**\n"
         cat_caption += f"⏳`Owner Name:` {DEFAULTUSER}\n"   
         cat_caption += f"⏳`Modified by:` [ԹԺՐԹՐ #̸M̸a̸s̸k̸ G̸a̸n̸g̸](t.me/AdrarHussain)\n\n"         
         cat_caption += f"**[⚜️DEPLOY CATUSERBOT⚜️](https://github.com/Adrarofficial/catuserbot)**"
         await borg.send_file(alive.chat_id, CAT_IMG, caption=cat_caption)
         await alive.delete()
    else:
        await alive.edit("🚴‍♂️**MY BOT IS RUNNING SUCCESFULLY**\n\n"
                         "**Database Status: Databases Functioning Normally!**\n"
                         f"⏳`Telethon Version:` **{version.__version__}**\n"
                         f"⏳`Python Version:` **{python_version()}**\n"
                         f"⏳`Catuserbot Version:` **{catversion}**\n"
                         f"⏳`Cat Uptime:` **{uptime}**\n\n"                        
                         "**Cat is Always With You, My Masters!**\n"                                                
                         f"⏳`Owner Name:` {DEFAULTUSER}\n"
                         "⏳`Modified by:` [ԹԺՐԹՐ #̸M̸a̸s̸k̸ G̸a̸n̸g̸](t.me/AdrarHussain)\n\n"
                         f"**[⚜️DEPLOY CATUSERBOT⚜️](https://github.com/Adrarofficial/catuserbot)**"
                        )

CMD_HELP.update({"alive": "`.alive` :\
      \nUSAGE: Type .live to see wether your bot is working or not. "
}) 
