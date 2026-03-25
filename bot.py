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

# ========== HANDLER FUNKSIYALAR ==========
# O'zingizning handlerlaringizni shu yerga yozing
async def start(update, context):
    """/start komandasi uchun handler"""
    await update.message.reply_text(
        "👋 Salom! Bot ishga tushdi!\n\n"
        "Bot to'g'ri ishlayapti."
    )
    logger.info(f"User {update.effective_user.id} started the bot")

async def echo(update, context):
    """Matnli xabarlar uchun handler"""
    user_text = update.message.text
    await update.message.reply_text(f"Siz yozdingiz: {user_text}")

async def help_command(update, context):
    """Yordam komandasi"""
    await update.message.reply_text(
        "🤖 Bot komandalari:\n"
        "/start - Botni ishga tushirish\n"
        "/help - Yordam\n"
        "Matn yozing - Men sizga qaytaraman"
    )

# ========== MAIN FUNKSIYA ==========
async def main():
    """Botni ishga tushirish"""
    # Application yaratish
    app = Application.builder().token(TOKEN).build()
    
    # Handlerlarni qo'shish
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    
    # Render muhitidan port olish
    port = int(os.environ.get("PORT", 8443))
    
    # 🔥 APP URL'INI O'ZINGIZGA MOSLAB O'ZGARTIRING
    # Masalan: app nomi "mybot" bo'lsa:
    YOUR_APP_URL = "https://sizning-app-nomiz.onrender.com"  # ← SHUNI O'ZGARTIRING!
    
    webhook_url = f"{YOUR_APP_URL}/{TOKEN}"
    
    logger.info("=" * 50)
    logger.info("🤖 Bot ishga tushmoqda...")
    logger.info(f"📡 Port: {port}")
    logger.info(f"🔗 Webhook URL: {webhook_url}")
    logger.info(f"🐍 Python versiya: 3.11.9")
    logger.info("=" * 50)
    
    try:
        # Webhookni o'rnatish
        await app.bot.set_webhook(url=webhook_url)
        logger.info("✅ Webhook muvaffaqiyatli o'rnatildi")
        
        # Webhook serverni ishga tushirish
        await app.run_webhook(
            listen="0.0.0.0",
            port=port,
            url_path=TOKEN,
            webhook_url=webhook_url,
            drop_pending_updates=True,
        )
    except Exception as e:
        logger.error(f"❌ Xatolik: {e}")
        raise

if __name__ == "__main__":
    # Python 3.11.9 uchun asyncio.run() ishlatiladi
    asyncio.run(main())
