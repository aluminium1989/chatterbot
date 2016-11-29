from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
import json

class Model(object):
    def __init__(self, updater):
        self.updater = updater
        self.data = []
        self.startPolling()
        self.bindEvents()
        self.chatbot = ChatBot('Familiaris Alumnus', trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
                               logic_adapters=[
                                   "chatterbot.adapters.logic.MathematicalEvaluation",
                                   "chatterbot.adapters.logic.TimeLogicAdapter",
                                   "chatterbot.adapters.logic.ClosestMatchAdapter"
                               ],
                               output_format='text')

        self.chatbot.set_trainer(ChatterBotCorpusTrainer)

        self.chatbot.train(
            "chatterbot.corpus.russian"
        )
        self.chatbot.train(
            "chatterbot.corpus.english"
        )

    def bindEvents(self):
        self.dispatcher().add_handler(CommandHandler('start', self.start))
        self.dispatcher().add_handler(MessageHandler(Filters.text, self.echo))

    def startPolling(self):
        self.updater.start_polling()

    def dispatcher(self):
        return self.updater.dispatcher

    def start(self, bot, update):
        bot.sendMessage(chat_id=update.message.chat_id, text="Hello %s" % update.message.from_user.first_name)

    def echo(self, bot, update):
        response = self.chatbot.get_response(update.message.text)
        bot.sendMessage(chat_id=update.message.chat_id, text=response)