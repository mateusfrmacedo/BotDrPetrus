from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import logging
import random

# Substitua pelo seu token do BotFather
TOKEN = "7886734344:AAF3bMlpsaF-dG_VUQoKN6A2mzw_GyJnQ9I"

# Frases do Dr. Petrus extraídas do JSON
frases_petrus = [
    "Uai", "Gol", "Pq", "bora?", "Ta osso", "vou ali no terreno guardar o carro", 
    "E o polera? Zero?", "Meu também foi embora", "A man, cara ofertou um valor bacana", "N teve jeito kk"
]

# Função para gerar uma resposta no estilo do Dr. Petrus
def resposta_estilo_petrus():
    return random.choice(frases_petrus)

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Fala, man! Sou o bot do Dr. Petrus. Manda uma mensagem aí!")

def handle_message(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text
    response = resposta_estilo_petrus()
    update.message.reply_text(response)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
