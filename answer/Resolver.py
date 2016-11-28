from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters


class Model(object):
    def __init__(self, updater):
        self.updater = updater
        self.data = []
        self.startPolling()
        self.bindEvents()

    def bindEvents(self):
        self.dispatcher().add_handler(self.start)
        self.dispatcher().add_handler(self.echo)

    def startPolling(self):
        self.updater.start_polling()

    def dispatcher(self):
        return self.updater.dispatcher

    def start(self, bot, update):
        bot.sendMessage(chat_id=update.message.chat_id, text="Hello %s" % update.message.from_user.first_name)

    def echo(self, bot, update):
        bot.sendMessage(chat_id=update.message.chat_id, text=update.message.text)