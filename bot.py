import asyncio

from aiogram import Bot, Dispatcher

from config_data.config import load_config
from handlers import start_handlers, new_estimate_handlers, other_handlers
from keyboards.menu import set_main_menu
from services.orm.bd_model import create_bd

API_TOKEN = load_config().tg_bot.token


async def main():
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher()
    dp.startup.register(set_main_menu)

    dp.include_router(start_handlers.router)
    dp.include_router(new_estimate_handlers.router)
    dp.include_router(other_handlers.router)
    
    print("/nРаботаем.../n")


# Запускаем бота и пропускаем все накопленные входящие
    # Да, этот метод можно вызвать даже если у вас поллинг  
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)



if __name__ == '__main__':
    # create_bd()
    asyncio.run(main())
