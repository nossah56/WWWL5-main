import re

from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest as unblock

from WWWL5 import WWWL5
from WWWL5.helpers.functions import delete_conv

from ..sql_helper.globals import addgvar, gvarstatus


async def ai_api(event):
    token = gvarstatus("AI_API_TOKEN") or None
    if not token:
        chat = "@Mailsasabot"
        token = "6828682522:AAHGaysM_HsNFVlBM-Lv8KmXAaCwvGFZxys"
        async with event.client.conversation(chat) as conv:
            try:
                purgeflag = await conv.send_message("/start")
            except YouBlockedUserError:
                await WWWL5(unblock("Kukichatbot"))
                purgeflag = await conv.send_message("/start")
            await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
            await conv.send_message("/token")
            respond = await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
            await delete_conv(event, chat, purgeflag)
            if rgxtoken := re.search(r"(?:API: )(.+)(?: Do)", respond.message):
                token = rgxtoken[1]
            addgvar("AI_API_TOKEN", token)
    return token
