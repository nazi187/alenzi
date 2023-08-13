##By Reda Telegram: @rd0r0
import asyncio
import logging
import os
import random
import time
from . import BOTLOG, BOTLOG_CHATID
from datetime import datetime
from telethon import events
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.types import InputPeerChannel
from telethon.errors import ChannelPrivateError
from telethon.utils import get_peer_id
from HuRe import l313l
from telethon import types
from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import _cattools, _catutils, _format, parse_pre, reply_id
from telethon.utils import get_display_name

slist = None

async def spam_function(event, HuRe, l3313l, sleeptimet, rp):
    global slist
    DelaySpam = False
    counter = int(l3313l[0])
    
    if len(rp) > 2:
        if HuRe:
            for _ in range(counter):
                if gvarstatus("spamworkk") is None:
                    return
                spam_message = random.choice(list(filter(None, slist)))
                await HuRe.reply(spam_message.message)
                await asyncio.sleep(sleeptimet)
        if BOTLOG:
            if DelaySpam is not True:
                if event.is_private:
                    await event.client.send_message(
                        BOTLOG_CHATID,
                        "**⌔∮ التڪرار  **\n"
                        + f"**⌔∮ تم تنفيذ التكرار بنجاح في ** [المستخدم](tg://user?id={event.chat_id}) **الدردشة مع** {counter} **عدد المرات مع الرسالة أدناه**",
                    )
                else:
                    await event.client.send_message(
                        BOTLOG_CHATID,
                        "**⌔∮ التڪرار  **\n"
                        + f"**⌔∮ تم تنفيذ التكرار بنجاح في ** {get_display_name(await event.get_chat())}(`{event.chat_id}`) **مع** {counter} **عدد المرات مع الرسالة أدناه**",
                    )
            elif event.is_private:
                await event.client.send_message(
                    BOTLOG_CHATID,
                    "**⌔∮ التكرار الوقتي **\n"
                    + f"**⌔∮ تم تنفيذ التكرار الوقتي  بنجاح في ** [المستخدم](tg://user?id={event.chat_id}) **الدردشة مع** {counter} **عدد المرات مع الرسالة أدناه مع التأخير** {sleeptimet} ** الثواني **",
                )
            else:
                await event.client.send_message(
                    BOTLOG_CHATID,
                    "**⌔∮ التكرار الوقتي **\n"
                    + f"**⌔∮ تم تنفيذ التكرار الوقتي  بنجاح في ** {get_display_name(await event.get_chat())}(`{event.chat_id}`) **مع** {counter} **عدد المرات مع الرسالة أدناه مع التأخير** {sleeptimet} ** الثواني **",
                )
    elif len(rp) == 2:
        
        for _ in range(counter):
            if gvarstatus("spamworkk") is None:
                return
            spam_message = random.choice(list(filter(None, slist)))
            await event.client.send_message(event.chat_id, spam_message.message)
            await asyncio.sleep(sleeptimet)


@l313l.ar_cmd(pattern="سب")
async def spammer(event):
    global slist
    reply = await event.get_reply_message()
    r = "rd"
    if reply:
    	r = "redaaa"
    input_str = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
    try:
        channel = await l313l.get_entity(input_str[2])
        slist = await l313l.get_messages(channel, limit=None)
        
    except Exception as er:
    	return await l313l.send_message(BOTLOG_CHATID, f"حدث خطأ\n {er}")
    
    try:
        sleeptimet = sleeptimem = int(input_str[0])
    except Exception:
        return await edit_delete(
            event, "⌔∮ يجب استخدام كتابة صحيحة الرجاء التاكد من الامر اولا ⚠️"
        )
    l3313l = input_str[1:]
    await event.delete()
    addgvar("spamworkk", True)
    await spam_function(event, reply, l3313l, sleeptimet, r)

@l313l.ar_cmd(pattern="ايقاف السب")
async def reda(event):
    await event.delete()
    if gvarstatus("spamworkk") is not None and gvarstatus("spamworkk"):
        delgvar("spamworkk")
