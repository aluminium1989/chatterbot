import logging
from telegram.ext import Updater
from telegram.ext import CommandHandler

updater = Updater(token='284902130:AAHSfbRM7SeUX0J1CYS5f9DVvduAcKzPWNs')
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
updater.start_polling()