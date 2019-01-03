import logging
import os
import requests
import json
import sqlite3
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
    video_handler = CommandHandler('updates', updates)
    echo_handler = MessageHandler(Filters.text, echo)
    unknown_handler = MessageHandler(Filters.command, unknown)

    #Start handlers
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(whoami_handler)
    dispatcher.add_handler(updates_handler)
    dispatcher.add_handler(echo_handler)
    dispatcher.add_handler(unknown_handler)

    updater.start_polling()

def loggingSetup():

    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )

def updates (bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Looking for new updates ...")

    conn = sqlite3.connect('/data/motion/db/motion.sqlite')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM security WHERE event_ack = 0')

    for reg in cursor:
        bot.send_message(chat_id=update.message.chat_id, text=reg)
        print(reg)

    #bot.send_video(chat_id=update.message.chat_id, video=open('/app/video/example/sample.mp4', 'rb'), supports_streaming=True)

    cursor.close()
    conn.close()

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