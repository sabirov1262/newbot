import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters
from telegram.error import TelegramError

from database import init_db
from handlers import start_handler, message_handler, button_handler
from config import BOT_TOKEN, WEBHOOK_HOST, PORT

# LOG
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Global application object
app = None

async def setup_application():
    """Application ni sozlash"""
    global app
    app = Application.builder().token(BOT_TOKEN).build()
    
    # Handlerlar
    app.add_handler(CommandHandler("start", start_handler))
    app.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, message_handler))
    app.add_handler(CallbackQueryHandler(button_handler))
    
    return app

async def main():
    """Asosiy funksiya"""
    global app
    
    # Database init
    await init_db()
    logger.info("✅ Database tayyor!")
    
    # Application setup
    app = await setup_application()
    
    logger.info("Bot ishga tushdi...")
    
    try:
        # Webhook orqali ishga tushirish
        await app.initialize()
        await app.updater.start_webhook(
            listen="0.0.0.0",
            port=PORT,
            url_path=BOT_TOKEN,
            webhook_url=f"{WEBHOOK_HOST}/{BOT_TOKEN}",
            drop_pending_updates=True
        )
        
        # Botni ishga tushirish
        logger.info(f"Bot webhook orqali ishga tushdi: {WEBHOOK_HOST}/{BOT_TOKEN}")
        
        # Keep the bot running
        await asyncio.Event().wait()
        
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot to'xtatildi")
    except Exception as e:
        logger.error(f"Xatolik: {e}")
    finally:
        if app:
            await app.shutdown()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
