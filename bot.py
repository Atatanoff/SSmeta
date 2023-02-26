import asyncio

from aiogram import Bot, Dispatcher

from config_data.config import load_config
from handlers import start_hendlers, new_estimate_hendlers
from keyboards.menu import set_main_menu

API_TOKEN = load_config().tg_bot.token

async def main():
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher()
    dp.startup.register(set_main_menu)

    dp.include_router(start_hendlers.router)
    dp.include_router(new_estimate_hendlers.router)

# Запускаем бота и пропускаем все накопленные входящие
    # Да, этот метод можно вызвать даже если у вас поллинг  
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
