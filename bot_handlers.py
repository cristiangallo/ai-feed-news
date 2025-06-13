from telegram import Update
from telegram.ext import ContextTypes
import preferences

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,
        text="¡Hola! Recibirás el resumen diario a las 8 a.m. Usa +tema o -tema para elegir.")

async def add_topic(update: Update, context: ContextTypes.DEFAULT_TYPE):
    topic = context.args[0]
    preferences.add_topic(update.effective_chat.id, topic)
    await update.message.reply_text(f"✅ Tema *{topic}* agregado.", parse_mode='Markdown')

async def remove_topic(update: Update, context: ContextTypes.DEFAULT_TYPE):
    topic = context.args[0]
    preferences.remove_topic(update.effective_chat.id, topic)
    await update.message.reply_text(f"❌ Tema *{topic}* excluido.", parse_mode='Markdown')

async def list_topics(update: Update, context: ContextTypes.DEFAULT_TYPE):
    plus, minus = preferences.get_prefs(update.effective_chat.id)
    msg = "*Tus temas actuales:*\n"
    msg += "✔️ Incluidos: " + (', '.join(plus) if plus else 'ninguno') + '\n'
    msg += "🚫 Excluidos: " + (', '.join(minus) if minus else 'ninguno')
    await update.message.reply_text(msg, parse_mode='Markdown')
