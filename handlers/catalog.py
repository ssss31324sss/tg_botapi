from aiogram import Router, F
from aiogram.types import Message
from keyboards.catalog import catalog_keyboard

router = Router()

@router.message(F.text == "📦 Каталог")
async def open_catalog(message: Message):
    await message.answer(
        "🛍 <b>Для покупки товара выберите из меню-кнопок ниже:</b>",
        reply_markup=catalog_keyboard,
        parse_mode="HTML"
    )
