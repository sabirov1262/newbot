import logging
import os
import asyncio
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackQueryHandler, Filters
from database import init_db
from handlers import start_handler, button_handler, message_handler, admin_check

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Environment Variables
BOT_TOKEN = os.environ.get("BOT_TOKEN")
SUPER_ADMIN_ID = int(os.environ.get("SUPER_ADMIN_ID", 0))

def main():
    # Async DB ni ishga tushirish (Render va eski PTB uchun)
    asyncio.run(init_db())  # init_db() async bo‘lsa shunday chaqiramiz

    # Updater yaratish
    updater = Updater(token=BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    # Handlerlar qo‘shish
    dp.add_handler(CommandHandler("start", start_handler))
    dp.add_handler(CallbackQueryHandler(button_handler))
    dp.add_handler(MessageHandler(Filters.all & ~Filters.command, message_handler))

    logger.info("Bot ishga tushdi...")

    # Polling orqali ishga tushirish
    updater.start_polling()
    updater.idle()  # Botni ishlashda ushlab turadi

if __name__ == "__main__":
    main()
