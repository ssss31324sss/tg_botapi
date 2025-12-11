from aiogram import Router, F
from aiogram.types import Message

from keyboards import menu_keyboard
from database.db import add_user

router = Router()


@router.message(F.text.in_({"/start", "Меню"}))
async def start(message: Message):
    # сохраняем пользователя
    add_user(
        tg_id=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name
    )

    await message.answer(
        "Добро пожаловать в RE Shop 💎\n\nВыберите действие:",
        reply_markup=menu_keyboard
    )
