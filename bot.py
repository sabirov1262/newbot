import logging
import os

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

# LOG
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# ENV
BOT_TOKEN = os.environ.get("BOT_TOKEN")
WEBHOOK_HOST = os.environ.get("WEBHOOK_HOST")  # https://newbot-fwh4.onrender.com
PORT = int(os.environ.get("PORT", 10000))


# START HANDLER
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salom! Bot ishlayapti 🚀")


# MESSAGE HANDLER
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text)


# MAIN
def main():
    # Application yaratish
    app = Application.builder().token(BOT_TOKEN).build()

    # Handlerlar qo‘shish
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    logger.info("Bot ishga tushdi...")

    # Webhook orqali ishga tushurish
    app.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        webhook_url=f"{WEBHOOK_HOST}/{BOT_TOKEN}",
        drop_pending_updates=True
    )


if __name__ == "__main__":
    main()
