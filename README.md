# AlanProCactusTelegramBot.V-3

**Telegram Bot** that provides various information about the YouTube blogger **Alan Pro Cactus**.

Live bot: [@AlanProKaktusBot](https://t.me/AlanProKaktusBot)

---

## ✨ Features

- Get latest information and updates about Alan Pro Cactus
- Multi-language support (change language anytime)
- User registration and preferences saved in SQLite
- Beautiful bot interface with photos and descriptions
- Admin-only secret settings
- Fast and efficient code structure
- Smooth user experience from the first start

---

## 🛠 Tech Stack

| Technology              | Purpose                              |
|------------------------|--------------------------------------|
| **Python**             | Main programming language            |
| **pyTelegramBotAPI**   | Telegram Bot API                     |
| **SQLite3**            | User database (registration, language, status) |
| **Modular Architecture**| Clean separation of concerns         |

---

## 📁 Project Structure

```bash
.
├── data/
│   ├── database/           # SQLite database
│   ├── files/              # Static files
│   ├── locale/             # Multi-language texts
│   ├── photos/             # Bot images
│   └── util/               # Utilities
├── domain/
│   ├── entryPoint/         # Bot initialization
│   ├── functions/          # Main bot commands and handlers
│   └── mainCode/           # Core logic
└── main.py                 # Entry point (or similar)
