from aiogram import Router, F
from aiogram.types import Message
from keyboards.menu import menu_keyboard
from database.db import get_user, get_purchases

router = Router()

@router.message(F.text == "👤 Личный кабинет")
async def profile(message: Message):
    tg_id = message.from_user.id
    user = get_user(tg_id)

    if not user:
        await message.answer(
            "❌ Пользователь не найден.\n\n"
            "Нажмите /start",
            reply_markup=main_menu
        )
        return

    _, tg_id, username, first_name, purchases, balance = user
    purchases_list = get_purchases(tg_id)

    history = "—"
    if purchases_list:
        history = ""
        for name, price, date in purchases_list[:5]:
            history += f"• {name} — {price} ₽ ({date})\n"

    await message.answer(
        f"👤 <b>Личный кабинет</b>\n\n"
        f"🆔 ID: <code>{tg_id}</code>\n"
        f"👤 Имя: {first_name}\n"
        f"🔗 Username: @{username if username else 'не указан'}\n\n"
        f"📦 Покупок: {purchases}\n"
        f"💳 Баланс: {balance} ₽\n\n"
        f"🧾 <b>История покупок:</b>\n"
        f"{history}",
        reply_markup=main_menu,
        parse_mode="HTML"
    )
