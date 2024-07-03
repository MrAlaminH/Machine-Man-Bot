
# AI Assistant Telegram Bot- Machine Man

This Telegram bot leverages powerful language models to provide AI-powered functionalities, including text generation, image creation.

## Features

- Text generation using GPT-3.5 and LLaMA 3 models
- Image generation with playground-v2.5, kandinsky-3.1, SDXL
- User management and chat history
- Admin broadcast functionality

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7+
- A Telegram Bot Token (obtainable from [@BotFather](https://t.me/BotFather))
- An OpenAI API key

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/Machine-Man-Bot.git
   cd Machine-Man-Bot
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root and add your credentials:
   ```
   BOT_TOKEN=your_telegram_bot_token
   OPENAI_API_KEY=your_openai_api_key
   OPENAI_API_BASE=your_base_link
   ```

## Usage

To start the bot, run:

```
python main.py
```

### Available Commands

- `/start`: Initialize the bot and receive a welcome message
- `/help`: Get detailed instructions on how to use the bot
- `/clear`: Clear your conversation history
- `/image1`: Generate an image using the SDXL model
- `/image2`: Generate an image using the Kandinsky 3.1 model
- `/image3`: Generate an image using the Playground v2.5 model
- `/broadcast`: Send a message to all users (admin only)

### Text Generation

- Start your message with `!` to use GPT-3.5 for text generation
- Start your message with `$` to use LLaMA 3 for text generation

### Image Generation

Use the `/image1`, `/image2`, or `/image3` commands followed by your image description.

## Configuration

You can modify the `config.py` file to change various settings such as the database name, admin username, and more.

## Contributing

Contributions to improve the bot are welcome. Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## Contact

Bot Developer - [@Alamin_H](https://t.me/Alamin_H)
To use The Demo Try here: [@Machine_ManBot](https://t.me/Machine_ManBot)

