from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from keyboards.product import product_keyboard
from keyboards.catalog import catalog_keyboard

router = Router()

PRODUCTS = {
    "nitro_1": {
        "name": "💎 Discord Nitro FULL — 1 месяц",
        "price": "499 ₽",
        "desc": "✅ Полный доступ\n⏳ 30 дней\n⚡ Мгновенная выдача"
    },
    "nitro_6": {
        "name": "🎁 Discord Nitro FULL — 6+6 месяцев",
        "price": "4799 ₽",
        "desc": "✅ 12 месяцев\n🎁 +6 месяцев в подарок\n⚡ Автовыдача"
    },
    "nitro_12": {
        "name": "🔥 Discord Nitro FULL — 1 год",
        "price": "5399 ₽",
        "desc": "✅ 12 месяцев\n⚡ Полный функционал"
    }
}

@router.message(F.text.contains("Discord Nitro"))
async def open_product(message: Message):
    if "1 месяц" in message.text:
        pid = "nitro_1"
    elif "6" in message.text:
        pid = "nitro_6"
    else:
        pid = "nitro_12"

    p = PRODUCTS[pid]

    await message.answer(
        f"<b>{p['name']}</b>\n\n"
        f"{p['desc']}\n\n"
        f"💰 <b>{p['price']}</b>",
        reply_markup=product_keyboard(pid),
        parse_mode="HTML"
    )

@router.callback_query(F.data == "back_to_catalog")
async def back_catalog(call: CallbackQuery):
    await call.message.answer(
        "🛍 Выберите товар:",
        reply_markup=catalog_keyboard
    )
    await call.answer()
    
from database.db import add_purchase

@router.callback_query(F.data.startswith("buy:"))
async def fake_buy(call):
    pid = call.data.split(":")[1]

    PRODUCTS = {
        "nitro_1": ("Discord Nitro 1 месяц", 499),
        "nitro_6": ("Discord Nitro 6+6", 4799),
        "nitro_12": ("Discord Nitro 12 месяцев", 5399),
    }

    name, price = PRODUCTS[pid]

    add_purchase(
        tg_id=call.from_user.id,
        product_id=pid,
        product_name=name,
        price=price
    )

    await call.message.answer(
        f"✅ <b>Покупка сохранена (тест)</b>\n\n"
        f"{name}\n"
        f"💰 {price} ₽",
        parse_mode="HTML"
    )
    await call.answer()
