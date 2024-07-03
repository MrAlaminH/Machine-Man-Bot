from aiogram import Bot
from aiogram.types import BotCommand

async def set_bot_commands(bot: Bot):
    commands = [
        BotCommand(command="/help", description="Get Help for instructions."),
        BotCommand(command="/clear", description="Clear your context window"),
        BotCommand(command="/image1", description="Generate Image with Sdxl"),
        BotCommand(command="/image2", description="Generate Image with Kandinsky-3.1"),
        BotCommand(command="/image3", description="Generate Image with Playground-v2.5"),
        BotCommand(command="/start", description="Start the bot again"),
    ]
    await bot.set_my_commands(commands)

async def send_user_guide(bot: Bot, chat_id: int):
    user_guide = """
    📚 User Guide 📚

👋 Getting Started
- Start the Bot: Send `/start` to begin.
- Get Help: Send `/help` for instructions.

🖼️ Generating Images
- `/image1`: Generate landscape images.
- `/image2`: Generate abstract art images.
- `/image3`: Generate playful images.

🤖 AI Text Generation
- Start with `!` for stories, facts, and more by GPT4.
- Start with `$` for summaries and insights etc by llama3-70B.

📝 Commands
- Ensure your commands start with `/image`, `!`, or `$`.
- Must add a description for image generation.

🔍 Additional Info
- Use the appropriate command for your task.
- Follow the format for accurate results.
- Use /clear command to clear the chat history and start with new chat tab.

📞 Contact Owner
For assistance or feedback, contact the bot administrator:
- Email: alamin@sodality.xyz
- Telegram: @Alamin_H

🚀 **Get Started Now!**
Start by sending `/start` and explore the bot's capabilities!
    """
    await bot.send_message(chat_id, user_guide)

async def send_processing_message(bot: Bot, chat_id: int):
    return await bot.send_message(chat_id, 'I am processing your request...')

async def send_error_message(bot: Bot, chat_id: int):
    return await bot.send_message(chat_id, 'An error occurred. Please try again later.')