import asyncio
import logging
import os
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters
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
WEBHOOK_HOST = os.environ.get("webhook_host")  # https://newbot-fwh4.onrender.com
PORT = int(os.environ.get("PORT", 5000))      # Render avtomatik PORT beradi

async def main():
    await init_db()
    
    app = Application.builder().token(BOT_TOKEN).build()
    
    # Handlerlar
    app.add_handler(CommandHandler("start", start_handler))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, message_handler))
    
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
