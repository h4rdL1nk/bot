import logging
import os
import requests
import json
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

def main():

    telegram_token = os.environ['TOKEN']

    updater = Updater(token=telegram_token)
    dispatcher = updater.dispatcher

    #Declare handlers
    start_handler = CommandHandler('start', start)
    whoami_handler = CommandHandler('whoami', whoami)
    echo_handler = MessageHandler(Filters.text, echo)
    unknown_handler = MessageHandler(Filters.command, unknown)

    #Start handlers
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(whoami_handler)
    dispatcher.add_handler(echo_handler)
    dispatcher.add_handler(unknown_handler)

    updater.start_polling()

def loggingSetup():

    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )

def whoami(bot, update):
    r = requests.get('http://ifconfig.co/json')

    bot.send_message(chat_id=update.message.chat_id, text="WHO")

    if r.status_code == 200:
        data = r.json()
        bot.send_message(chat_id=update.message.chat_id, text=data['city'] + "(" + data['country'] + ") " + data['ip'])
    else:
        bot.send_message(chat_id=update.message.chat_id, text="ifconfig.co returned bad HTTP_CODE :(")

def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")

def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")


if __name__ == "__main__":
    main()