from aiogram import Router, F
from aiogram.types import Message
from keyboards.menu import menu_keyboard

router = Router()

@router.message(F.text == "ℹ️ О магазине")
async def about_shop(message: Message):
    await message.answer(
        "💎 <b>О нашем магазине</b>\n\n"
        "Мы продаём цифровые товары с автоматической выдачей.\n"
        "✅ Быстро\n"
        "✅ Безопасно\n"
        "✅ Без посредников\n\n"
        "Работаем 24/7 🔥",
        reply_markup=menu_keyboard(),
        parse_mode="HTML"
    )
