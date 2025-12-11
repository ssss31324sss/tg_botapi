from aiogram import Router, F
from aiogram.types import Message
from keyboards.menu import main_menu

router = Router()

@router.message(F.text.in_({
    "ℹ️ О магазине",
    "📜 Правила"
}))
async def stub_info(message: Message):
    await message.answer(
        "🚧 <b>Раздел в разработке</b>\n\n"
        "Мы уже работаем над этим разделом.\n"
        "Совсем скоро он будет доступен ✅",
        reply_markup=main_menu,
        parse_mode="HTML"
    )
