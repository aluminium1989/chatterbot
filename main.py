import sys, getopt, logging
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from answer import Resolver

def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Hello %s" % update.message.from_user.first_name)


def echo(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text=update.message.text)


def main(argv):
    token = ''
    try:
        opts, args = getopt.getopt(argv, "ht:", ["token="])
    except getopt.GetoptError:
        print('test.py -t <token>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -t <token>')
            sys.exit()
        elif opt in ("-t", "--token"):
            token = arg

    # init logging
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    updater = Updater(token)
    updater.dispatcher

    answer = Resolver.Model(updater)

    # listen start button
    #start_handler = CommandHandler('start', start)
    #dispatcher.add_handler(start_handler)

    # listen messages
    #echo_handler = MessageHandler(Filters.text, echo)
    #dispatcher.add_handler(echo_handler)

    # start listening messages
    #updater.start_polling()


if __name__ == "__main__":
    main(sys.argv[1:])
