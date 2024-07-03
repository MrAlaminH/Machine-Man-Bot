from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from services.openai_service import generate_image, generate_text
from bot.utils import send_user_guide, send_processing_message, send_error_message
from bot.database import Database
from config import ADMIN_USERNAME

db = Database()
messages = {}

async def start_cmd(message: types.Message):
    try:
        username = message.from_user.username if message.chat.type == types.ChatType.PRIVATE else message.chat.title
        chat_id = message.chat.id
        chat_type = message.chat.type
        db.add_user_or_group(username, chat_id, chat_type)
        messages[chat_id] = []
        await message.answer("👋 Hi I'm Machine Man Developed by @Alamin_H\n\n"
            "I'm here to assist you with various tasks using advanced AI models. Whether you need help generating images, crafting stories, or summarizing articles, I've got you covered!\n\n"
            "To get started, simply send me a message with one of the following commands:\n"
            "- `/start`: Initialize the bot and learn more about what I can do.\n"
            "- `/help`: Get detailed instructions on how to interact with me.\n\n"
            "Feel free to explore my capabilities and don't hesitate to reach out if you have any questions or need assistance. Let's make your experience with AI both fun and productive!\n\n"
            "Happy chatting! 🤖✨")
    except Exception as e:
        print(f'Error in start_cmd: {e}')

async def help_cmd(message: types.Message):
    try:
        await send_user_guide(message.bot, message.chat.id)
    except Exception as e:
        print(f'Error in help_cmd: {e}')

async def clear_cmd(message: types.Message):
    try:
        chat_id = message.chat.id
        if chat_id in messages:
            messages[chat_id] = []
            await message.answer("Conversation history cleared. You can now start a new chat.")
        else:
            await message.answer("No conversation history found.")
    except Exception as e:
        print(f'Error in clear_cmd: {e}')

async def broadcast_cmd(message: types.Message):
    if message.chat.type == types.ChatType.PRIVATE and message.from_user.username == ADMIN_USERNAME:
        try:
            broadcast_text = message.text.split(maxsplit=1)[1].strip()
            if not broadcast_text:
                await message.reply("Please provide a non-empty message to broadcast.")
                return

            success_count = 0
            failure_count = 0
            for chat_id in db.get_all_chat_ids():
                try:
                    await message.bot.send_message(chat_id, broadcast_text)
                    success_count += 1
                except Exception:
                    failure_count += 1

            await message.reply(f"Broadcast message sent to {success_count} chats. Failed to send to {failure_count} chats.")
        except Exception as e:
            print(f'Error in broadcast_cmd: {e}')
            await message.reply("An error occurred while broadcasting the message.")

async def handle_image_generation(message: types.Message, model_name: str):
    try:
        description = message.text.split(maxsplit=1)[1].strip() if len(message.text.split(maxsplit=1)) > 1 else ""
        if not description:
            await message.reply('Please add a description of the image after the command.')
            return

        processing_message = await send_processing_message(message.bot, message.chat.id)
        image_url = await generate_image(description, model_name)

        if image_url:
            await message.bot.send_photo(chat_id=message.chat.id, photo=image_url, reply_to_message_id=message.message_id)
        else:
            await message.reply('Failed to generate the image.')

        await processing_message.delete()
    except Exception as e:
        print(f'Error in handle_image_generation: {e}')
        await send_error_message(message.bot, message.chat.id)

async def handle_message(message: types.Message):
    try:
        user_message = message.text
        chat_id = message.chat.id      
        if user_message.startswith("!"):
            model_name = "gpt-3.5-turbo-0125"
            user_message = user_message[1:].strip()
        elif user_message.startswith("$"):
            model_name = "llama-3-70b-instruct"
            user_message = user_message[1:].strip()
        else:
            if message.chat.type == types.ChatType.PRIVATE:
                await message.reply("You're using me incorrectly. To learn how to use me properly, click `/help` for detailed instructions.")
            return

        if chat_id not in messages:
            messages[chat_id] = []

        messages[chat_id].append({"role": "user", "content": user_message})

        processing_message = await send_processing_message(message.bot, chat_id)
        await message.bot.send_chat_action(chat_id=chat_id, action="typing")

        response = await generate_text(messages[chat_id], model_name)

        if response:
            messages[chat_id].append({"role": "assistant", "content": response})
            await message.reply(response)
        else:
            await message.reply("I'm sorry, I couldn't generate a response. Please try again.")

        await processing_message.delete()

    except Exception as e:
        print(f'Error in handle_message: {e}')
        await send_error_message(message.bot, message.chat.id)

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_cmd, commands=['start'])
    dp.register_message_handler(help_cmd, commands=['help'])
    dp.register_message_handler(clear_cmd, commands=['clear'])
    dp.register_message_handler(broadcast_cmd, commands=['broadcast'])
    dp.register_message_handler(lambda m: handle_image_generation(m, "sdxl"), commands=['image1'])
    dp.register_message_handler(lambda m: handle_image_generation(m, "kandinsky-3.1"), commands=['image2'])
    dp.register_message_handler(lambda m: handle_image_generation(m, "playground-v2.5"), commands=['image3'])
    dp.register_message_handler(handle_message)