import os
import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Telegram Bot Token from BotFather
TELEGRAM_TOKEN = os.getenv("7047046491:AAF1LY-bLASYT7jco1-CP5hK8XM8JtNdFpc")

if not TELEGRAM_TOKEN:
    raise ValueError("Please set the TELEGRAM_TOKEN environment variable.")

# Function to handle start command
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("👾 Send me a URL from social media, and I'll download the content for you!")

# Function to handle URLs
def handle_url(update: Update, context: CallbackContext) -> None:
    url = update.message.text
    if "instagram.com" in url:
        content_url = download_instagram_content(url)
        if content_url:
            update.message.reply_text(f"🔗 Here's your content: {content_url}")
        else:
            update.message.reply_text("⚠️ Could not download content from this URL.")
    else:
        update.message.reply_text("❌ Unsupported URL. Please send an Instagram URL.")

# Function to download Instagram content
def download_instagram_content(url):
    try:
        # Replace with the actual API URL
        response = requests.get(f"https://instagram-downloader-api-url.com/?url={url}")
        if response.status_code == 200:
            # Assuming the API returns the direct URL to the content
            return response.json().get("download_url")  # Adjust based on actual API response
    except Exception as e:
        print(f"Error: {e}")
    return None

# Main function to run the bot
def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Add command and message handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_url))

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
