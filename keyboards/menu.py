from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def menu_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📦 Каталог")],
            [
                KeyboardButton(text="👤 Личный кабинет"),
                KeyboardButton(text="ℹ️ О магазине")
            ],
            [KeyboardButton(text="❓ Помощь")]
        ],
        resize_keyboard=True
    )
