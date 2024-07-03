import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import BOT_TOKEN
from bot.handlers import register_handlers
from bot.utils import set_bot_commands
from middlewares.auth_middleware import AuthMiddleware

logging.basicConfig(level=logging.INFO)

async def main():
    bot = Bot(token=BOT_TOKEN)
    storage = MemoryStorage()
    dp = Dispatcher(bot, storage=storage)

    # Register middlewares
    dp.middleware.setup(AuthMiddleware())

    # Register handlers
    register_handlers(dp)

    # Set bot commands
    await set_bot_commands(bot)

    # Start polling
    await dp.start_polling()

if __name__ == '__main__':
    asyncio.run(main())