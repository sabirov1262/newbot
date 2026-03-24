# 🎬 KINOLAR BOT — To'liq Telegram Kino Bot

## 📋 XUSUSIYATLAR

### 👤 Foydalanuvchi uchun:
- Kino kodi orqali kinolarni olish
- Majburiy obuna kanallarini tekshirish
- Deep link orqali kino olish (`/start film001`)
- Premium a'zolik

### 👮 Admin uchun:
- **📊 Statistika** — Foydalanuvchilar, kinolar, ko'rishlar
- **📨 Xabar yuborish** — Oddiy va Forward broadcast
- **🎬 Kinolar** — Qo'shish, tahrirlash, o'chirish, ro'yxat
- **🔐 Kanallar** — Majburiy obuna kanallarini boshqarish (3 tur)
- **👮 Adminlar** — Admin qo'shish/o'chirish
- **⚙️ Sozlamalar** — Ulashish, To'lov tizimlari, Premium

### ⭐ Premium tizimi:
- Premium tariflar (nom, muddat, narx)
- Foydalanuvchiga premium berish
- Premium foydalanuvchilar ro'yxati
- Premium holat (yoqish/o'chirish)

### 🔐 Kanal turlari:
- **Ommaviy/Shaxsiy** — Kanal/Guruh (obuna tekshiriladi)
- **Shaxsiy/So'rovli havola** — Invite link
- **Oddiy havola** — Instagram, YouTube va boshqalar

---

## 🚀 O'RNATISH

### 1. Faylllarni yuklab oling
```
kinobot/
├── bot.py
├── config.py
├── database.py
├── handlers.py
├── admin_handlers.py
├── movie_handlers.py
├── channel_handlers.py
├── tariff_handlers.py
├── broadcast_handlers.py
├── keyboards.py
├── states.py
└── requirements.txt
```

### 2. Requirements o'rnatish
```bash
pip install -r requirements.txt
```

### 3. config.py ni sozlang
```python
BOT_TOKEN = "YOUR_BOT_TOKEN"  # @BotFather dan oling
SUPER_ADMIN_ID = 123456789    # Sizning Telegram ID
```

### 4. Botni ishga tushiring
```bash
python bot.py
```

---

## 💡 FOYDALANISH

### Kino qo'shish:
1. Admin panelida **🎬 Kinolar** → **📥 Kino yuklash**
2. Kod kiriting (masalan: `001`)
3. Nom kiriting
4. Tavsif kiriting (yoki `-`)
5. Video/Document faylni yuboring
6. ✅ Tayyor!

### Kanal qo'shish:
1. Botni kanalga **admin** qiling
2. **🔐 Kanallar** → **➕ Kanal qo'shish**
3. Tur tanlang
4. Kanal ID yoki username yuboring (`@mychannel`)

### Kino olish (foydalanuvchi):
- Bot ga kino kodini yuboring: `001`
- Yoki deep link: `t.me/YourBot?start=001`

---

## 🛠 TEXNIK MA'LUMOT

- **Database**: SQLite (aiosqlite) — yengil, server kerak emas
- **Fayllar**: Telegram serverida saqlanadi (file_id) — xotira sarflanmaydi
- **Asinxron**: python-telegram-bot v20 (asyncio)
- **Python**: 3.10+

---

## ⚙️ SOZLAMALAR

| Sozlama | Tavsif |
|---------|--------|
| `BOT_TOKEN` | BotFather tokeni |
| `SUPER_ADMIN_ID` | Asosiy admin ID |

---

## 📞 MUAMMO BO'LSA

1. Bot tokenini tekshiring
2. Super admin ID to'g'ri ekanligini tekshiring  
3. Kanal uchun botni admin qilganingizni tekshiring
4. `pip install -r requirements.txt` qaytadan bajaring
