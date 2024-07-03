from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from config import ADMIN_USERNAME

class AuthMiddleware(BaseMiddleware):
    async def on_process_message(self, message: types.Message, data: dict):
        if message.get_command() == '/broadcast' and message.from_user.username != ADMIN_USERNAME:
            await message.reply("You are not authorized to use this command.")
            raise CancelHandler()