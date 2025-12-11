from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def product_keyboard(product_id: str):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="✅ Купить",
                    callback_data=f"buy:{product_id}"
                )
            ],
            [
                InlineKeyboardButton(
                    text="⬅️ Назад",
                    callback_data="back_to_catalog"
                )
            ]
        ]
    )
