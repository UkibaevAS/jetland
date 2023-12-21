import os
import dotenv
import asyncio
from aiogram import Bot, Dispatcher, Router

from handlers import start, auth_users
from keyboard.set_menu import set_main_menu

dotenv.load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')


# Функция конфигурирования и запуска бота
async def main():
    # Создаем объекты бота и диспетчера
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    # Регистриуем роутеры в диспетчере
    dp.include_router(auth_users.router)
    dp.include_router(start.router)

    await set_main_menu(bot)  # Настраиваем главное меню бота

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
