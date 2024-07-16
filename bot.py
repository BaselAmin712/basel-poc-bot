from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = '7284725214:AAHrwfdFoSBTe6YQpN8rFLwt6Ou0yRYPEEU'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Hello! I am your bot. How can I help you?')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    help_text = (
        "Available commands:\n"
        "/start - Start the bot\n"
        "/help - Show this help message"
    )
    await update.message.reply_text(help_text)

def get_details() -> str:
    details_text = (
        "Here are the specific details you requested:\n"
        "1. Bot version: 1.0.0\n"
        "2. Developed by: Basel Amin\n"
        "3. Contact: baselamin712@gmail.com"
    )
    return details_text

async def details_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    details_text = get_details()
    await update.message.reply_text(details_text)

def main():
    # Create the Application and pass it your bot's token.
    application = ApplicationBuilder().token(TOKEN).build()

    # Register the /start command handler
    application.add_handler(CommandHandler("start", start))
    # Register the /help command handler
    application.add_handler(CommandHandler("help", help_command))
    # Register the /details command handler
    application.add_handler(CommandHandler("details", details_command))

    # Start the Bot
    application.run_polling()

if __name__ == '__main__':
    main()
