# Â©ItzExStar

import re
import aiohttp

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

BOT_TOKEN = "5872061153:AAG94E59a4QQYiFAwNbw9hZvUD7JAS-KKtI"
USERS_API = {}

Altron = Client('XShortener',
            api_id=18136872,
            api_hash="312d861b78efcd1b02183b2ab52a83a4",
            bot_token=BOT_TOKEN,
            workers=100
            )

print("\nððð©ð¥ð¨ð²ðð ðð®ðððð¬ð¬ðð®ð¥ð¥ð² ðð¤ð»\nMy Master ---> @ðð­ð³ðð±ðð­ðð«")


@Altron.on_message(filters.command('start') & filters.private)
async def start(_, message):
    TEXT = """
ð¤ **Êá´Êá´..!!! 
ââââââââââââââ
â __Éª'á´ á´ ÊÉªÉ´á´ ê±Êá´Êá´á´É´á´Ê Êá´á´. ê±á´É´á´ á´á´ ÊÉªÉ´á´ á´É´á´ Éª'ÊÊ É¢Éªá´ á´ Êá´á´ Êá´á´á´ Éªá´'ê± ê±Êá´Êá´á´É´á´á´ ÊÉªÉ´á´__.
ââââââââââââââ
**â ï¸ ÊÊ á´á´ê°á´á´Êá´ Eá´sÊSá´Ê'ê± á´á´Éª á´á´Ê á´É´á´ á´á´Éª á´ÊÊ á´Êá´ á´ê±á´á´ !**
â á´ê±á´ /help á´á´ É¢á´á´ á´á´Êá´ sÉªá´á´s á´á´Éª á´ÊÊ á´É´á´ á´á´Éª á´á´Ê â¹ï¸.
"""
    await message.reply_photo(
        photo="https://te.legra.ph/file/ba44ebf64af97947a867b.jpg",
        caption=TEXT,
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("â á´á´á´ á´Êá´á´á´Ê", url="https://t.me/ItzExStar"),
            ],
            [
                InlineKeyboardButton("â ê±á´á´á´á´Êá´", url="https://t.me/AltronChats"),
                InlineKeyboardButton("â á´Êá´É´É´á´Ê", url="https://t.me/TheAltron"),
            ],
            ]     
        )
    )
    USERS_API[message.chat.id] = {"API_KEY":"https://easysky.in/members/tools/api", "API_URL":"https://easysky.in/api"}


@Altron.on_message(filters.command('help') & filters.private)
async def help(_, message):
    HELP_TEXT = f"""
**á´á´Éª á´ÊÊ á´ê° ê±á´á´á´ ê±Éªá´á´ê± á´Êá´:**

â² **EasySky**
  â£ á´á´Éª á´ÊÊ: https://easysky.in/api
  â£ á´á´Éª á´á´Ê: https://easysky.in/members/tools/api

â² **Droplink**
  â£ á´á´Éª á´ÊÊ: https://droplink.co/api
  â£ á´á´Éª á´á´Ê: https://droplink.co/member/tools/api

â² **MdiskShortener**
  â£ á´á´Éª á´ÊÊ: https://mdiskshortner.link/api
  â£ á´á´Éª á´á´Ê: https://mdiskshortner.link/member/tools/api

â² **DuLink**
  â£ á´á´Éª á´ÊÊ: https://dulink.in/api
  â£ á´á´Éª á´á´Ê: https://dulink.in/member/tools/api

â² **GPLink**
  â£ á´á´Éª á´ÊÊ: https://gplinks.in/api
  â£ á´á´Éª á´á´Ê: https://gplinks.in/member/tools/api

â² **PdiskShortener**
  â£ á´á´Éª á´ÊÊ: https://pdiskshortener.com/api
  â£ á´á´Éª á´á´Ê: https://pdiskshortener.com/member/tools/api

â² **TnLink**
  â£ á´á´Éª á´ÊÊ: https://tnlink.in/api
  â£ á´á´Éª á´á´Ê: https://tnlink.in/member/tools/api

â² **ClickyFly**
  â£ á´á´Éª á´ÊÊ: https://clickyfly.com/api
  â£ á´á´Éª á´á´Ê: https://clickyfly.com/member/tools/api


 á´sá´ á´ÊÉªs á´á´á´á´á´É´á´s á´á´ sá´á´ Êá´á´Ê á´á´sá´á´á´ á´á´Éª á´á´Ê á´É´á´ á´ÊÊ:
  â² /key <á´á´Éª á´á´Ê>: á´á´ á´sá´ Êá´á´Ê á´á´sá´á´á´ á´á´Éª á´á´Ê
  â² /url <á´á´Éª á´ÊÊ>: á´á´ á´sá´ Êá´á´Ê á´á´sá´á´á´ á´á´Éª á´ÊÊ
"""
    await message.reply_text(HELP_TEXT)


@Altron.on_message(filters.command('key') & filters.private)
async def key(_, message):
  Key = message.text.split(" ")
  if len(Key) == 1:
    await message.reply_text("Â» ð¨ðð®ð´ð²: /key <á´á´Éª á´á´Ê>")
    return
  global USERS_API
  USERS_API[message.chat.id]["API_KEY"] = Key[1]
  await message.reply_text("Â» Êá´á´Ê á´á´ê±á´á´á´ á´á´Éª á´á´Ê Êá´ê± Êá´É´ ê±á´á´á´á´.")


@Altron.on_message(filters.command('url') & filters.private)
async def url(_, message):
  Url = message.text.split(" ")
  if len(Url) == 1:
    await message.reply_text("Â» ð¨ðð®ð´ð²: /url <á´á´Éª á´ÊÊ>")
    return
  global USERS_API
  USERS_API[message.chat.id]["API_URL"] = Url[1]
  await message.reply_text("Â» Êá´á´Ê á´á´ê±á´á´á´ á´á´Éª á´ÊÊ Êá´ê± Êá´É´ ê±á´á´á´á´.")


@Altron.on_message(filters.private & filters.text & filters.incoming)
async def link_handler(_, message):
    link_pattern = re.compile('https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,}', re.DOTALL)
    links = re.findall(link_pattern, message.text)
    if len(links) < 1:
        await message.reply("Â» É´á´ ÊÉªÉ´á´ê± ê°á´á´É´á´ ÉªÉ´ á´ÊÉªê± á´á´xá´.", quote=True)
        return
    for link in links:
        try:
            short_link = await get_shortlink(link, message.chat.id)
            await message.reply(f"Â» Êá´Êá´ Éªê± Êá´á´Ê ê±Êá´Êá´á´É´á´á´ ÊÉªÉ´á´\n\n**á´ÊÉªÉ¢ÉªÉ´á´Ê ÊÉªÉ´á´:** {link}\n**ê±Êá´Êá´á´É´á´á´ ÊÉªÉ´á´:** `{short_link}`", quote=True, disable_web_page_preview=True)
        except Exception as e:
            await message.reply(f'á´ÊÊá´Ê: `{e}`', quote=True)


async def get_shortlink(link, ID):
    url = USERS_API[ID]["API_URL"]
    params = {'api': USERS_API[ID]["API_KEY"], 'url': link}
    print(url, params)

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, raise_for_status=True) as response:
            data = await response.json()
            return data["shortenedUrl"]

Altron.run()
