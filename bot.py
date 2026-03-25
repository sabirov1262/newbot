import os
import asyncio
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, ContextTypes, filters

from database import init_db
from handlers import start_handler, message_handler, button_handler

# LOG
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# ENV
BOT_TOKEN = os.environ.get("BOT_TOKEN")
WEBHOOK_HOST = os.environ.get("WEBHOOK_HOST")
PORT = int(os.environ.get("PORT", 10000))

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN environment variable not set")
if not WEBHOOK_HOST:
    raise ValueError("WEBHOOK_HOST environment variable not set")

# MAIN
async def main():
    await init_db()  # Database tayyorlash

    app = Application.builder().token(BOT_TOKEN).build()

    # Handlerlar
    app.add_handler(CommandHandler("start", start_handler))
    app.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, message_handler))
    app.add_handler(CallbackQueryHandler(button_handler))

    logger.info("Bot ishga tushdi...")

    # Webhook orqali ishga tushirish
    await app.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        webhook_url=f"{WEBHOOK_HOST}/{BOT_TOKEN}",
        drop_pending_updates=True
    )

if __name__ == "__main__":
    asyncio.run(main())
