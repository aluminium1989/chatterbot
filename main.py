import sys, getopt, logging
from telegram.ext import Updater
from telegram.ext import CommandHandler


def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")


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

    updater = Updater(token)
    dispatcher = updater.dispatcher

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)
    updater.start_polling()


if __name__ == "__main__":
    main(sys.argv[1:])
