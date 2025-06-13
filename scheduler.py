import asyncio
from datetime import datetime, time as dtime
from preferences import load
from formatter import format_summary

async def scheduler(bot):
    while True:
        now = datetime.now()
        if now.hour == 15 and now.minute == 10 and now.weekday() < 5:
            prefs = load()
            for uid in prefs.keys():
                text = format_summary(uid)
                await bot.send_message(chat_id=int(uid), text=text, parse_mode='Markdown', disable_web_page_preview=True)
            await asyncio.sleep(60)
        await asyncio.sleep(30)
