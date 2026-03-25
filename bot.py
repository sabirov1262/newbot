import logging
import os
import asyncio
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# ========== TOKEN ==========
TOKEN = os.environ.get("TOKEN")
if not TOKEN:
    raise ValueError("TOKEN environment variable not set")

# ========== LOGGING ==========
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# ========== HANDLERS (o'zingizdagi handlerlarni qo'shing) ==========
# async def start(update, context):
#     await update.message.reply_text("Salom! Bot ishga tushdi.")
# 
# async def echo(update, context):
#     await update.message.reply_text(update.message.text)

async def main():
    """Botni webhook orqali ishga tushirish."""
    app = Application.builder().token(TOKEN).build()
    
    # Handlerlarni qo'shing (quyidagi qatorlarni oching yoki o'zingiznikini yozing)
    # app.add_handler(CommandHandler("start", start))
    # app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    
    # Render muhitidan port va URL olish
    port = int(os.environ.get("PORT", 8443))
    webhook_url = os.environ.get("RENDER_EXTERNAL_URL")
    
    if not webhook_url:
        logger.error("RENDER_EXTERNAL_URL environment variable not set")
        return
    
    logger.info(f"Starting webhook on port {port} with URL {webhook_url}/{TOKEN}")
    
    # Webhookni ishga tushirish
    await app.bot.set_webhook(url=f"{webhook_url}/{TOKEN}")
    
    # Webhook serverini ishga tushirish
    await app.run_webhook(
        listen="0.0.0.0",
        port=port,
        url_path=TOKEN,
        webhook_url=f"{webhook_url}/{TOKEN}",
        drop_pending_updates=True,
    )

if __name__ == "__main__":
    # Muhim: asyncio.run() ni faqat shu yerda ishlating
    asyncio.run(main())
