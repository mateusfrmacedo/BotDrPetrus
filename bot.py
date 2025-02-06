from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import logging

# Substitua pelo seu token do BotFather
TOKEN = "7886734344:AAF3bMlpsaF-dG_VUQoKN6A2mzw_GyJnQ9I"

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("ACABO O FREIII")

def handle_message(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text
    update.message.reply_text(f"Você disse: {user_message}")  # Aqui depois vamos usar o estilo do Dr. Petrus

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
