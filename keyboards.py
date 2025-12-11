from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📦 Купить товар")],
        [
            KeyboardButton(text="👤 Личный кабинет"),
            KeyboardButton(text="🆘 Помощь"),
        ],
        [
            KeyboardButton(text="💎 О магазине"),
            KeyboardButton(text="📜 Правила"),
        ]
    ],
    resize_keyboard=True,
    is_persistent=True
)
