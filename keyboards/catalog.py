from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

catalog_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="💎 Discord Nitro FULL — 1 месяц | 499 ₽")],
        [KeyboardButton(text="🔥 Discord Nitro FULL — 1 год | 5399 ₽")],
        [KeyboardButton(text="🎁 Discord Nitro FULL — 6 мес + 6 мес | 4799 ₽")],
        [KeyboardButton(text="⬅️ Назад")]
    ],
    resize_keyboard=True
)
