import os

# Bot token
BOT_TOKEN = os.environ.get("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN environment variable not set")

# Webhook sozlamalari
WEBHOOK_HOST = os.environ.get("WEBHOOK_HOST")
if not WEBHOOK_HOST:
    raise ValueError("WEBHOOK_HOST environment variable not set")

PORT = int(os.environ.get("PORT", 8080))

# Super admin ID
SUPER_ADMIN_ID = int(os.environ.get("SUPER_ADMIN_ID", 0))

# Fayl saqlash usuli
STORAGE_TYPE = "telegram"

# Bot nomi
BOT_NAME = "Kinobot"
