import asyncio
from telegram.ext import ApplicationBuilder, CommandHandler
import bot_handlers, scheduler

TOKEN = '7898601164:AAHbJwBxZ-_JAGclc6F9ZHE4aTCNrWw5mVw'
app = ApplicationBuilder().token(TOKEN).build()

# Comandos
app.add_handler(CommandHandler('start', bot_handlers.start))
app.add_handler(CommandHandler('temas', bot_handlers.list_topics))
app.add_handler(CommandHandler('add', bot_handlers.add_topic))
app.add_handler(CommandHandler('remove', bot_handlers.remove_topic))

async def main():
    asyncio.create_task(scheduler.scheduler(app.bot))
    await app.run_polling()

if __name__ == '__main__':
    import nest_asyncio
    nest_asyncio.apply()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

