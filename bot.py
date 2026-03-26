
import os
import threading
import logging
from http.server import HTTPServer, BaseHTTPRequestHandler

from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters

from database import init_db
from handlers import start_handler, button_handler, message_handler
from config import BOT_TOKEN


# 🔹 Mini web server (Render port uchun)
class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")

    def log_message(self, format, *args):
        return  # loglarni kamaytiradi


def run_web():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(("0.0.0.0", port), HealthHandler)
    server.serve_forever()


# 🔹 Logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


# 🔹 DB init
async def post_init(app: Application):
    await init_db()
    logger.info('✅ Database tayyor!')


# 🔹 Main bot
def main():
    # 🔥 MUHIM — web serverni ishga tushiramiz
    threading.Thread(target=run_web, daemon=True).start()

    app = (
        Application.builder()
        .token(BOT_TOKEN)
        .post_init(post_init)
        .build()
    )

    app.add_handler(CommandHandler('start', start_handler))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, message_handler))

    logger.info('🚀 Bot ishga tushdi...')
    app.run_polling(drop_pending_updates=True)


if __name__ == '__main__':
    main()

