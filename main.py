import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties

from config import BOT_TOKEN
from handlers.start import router as start_router
from handlers.profile import router as profile_router
from handlers.about import router as about_router
from handlers.product import router as product_router

from database.db import init_db


async def main():
    # Проверка: токен должен существовать
    if not BOT_TOKEN:
        raise ValueError("❌ BOT_TOKEN не найден! Добавь его в Render → Environment Variables.")

    # Инициализация бота
    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(parse_mode="HTML")
    )

    dp = Dispatcher()

    # Подключаем роутеры
    dp.include_router(start_router)
    dp.include_router(profile_router)
    dp.include_router(about_router)
    dp.include_router(product_router)

    # Инициализация базы данных
    init_db()

    print("🤖 Бот запущен…")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
