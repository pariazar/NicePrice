#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

"""
telegram bot for retrieving price of digital currencies
Developer : Hamed Pariazar 2020 
"""
import logging 
import json
import py_compile
import os

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
data_path = "../digital_currencies.json"
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def start(update, context):
    os.system("python getCost.py")  

    keyboard = [[InlineKeyboardButton("bitcoin", callback_data='1'),
                 InlineKeyboardButton("ethereum", callback_data='2')],
                 [InlineKeyboardButton("xrp", callback_data='3'),
                 InlineKeyboardButton("tether", callback_data='4')],
                 [InlineKeyboardButton("chainlink", callback_data='5'),
                 InlineKeyboardButton("stellar", callback_data='6')],
                 [InlineKeyboardButton("bitcoin-cash", callback_data='7'),
                 InlineKeyboardButton("litecoin", callback_data='8')],
                [InlineKeyboardButton("usd-coin", callback_data='9')],
                 [InlineKeyboardButton("eos", callback_data='10'),
                 InlineKeyboardButton("monero", callback_data='11')],[InlineKeyboardButton("tron", callback_data='12'),
                 InlineKeyboardButton("tezos", callback_data='13')],[InlineKeyboardButton("zcash", callback_data='14'),
                 InlineKeyboardButton("dash", callback_data='15')],
                 [InlineKeyboardButton("ethereum-classic", callback_data='16'),
                 InlineKeyboardButton("dai", callback_data='17')],[InlineKeyboardButton("0x", callback_data='18'),InlineKeyboardButton("orchid", callback_data='19')],
                [InlineKeyboardButton("bitcoin-sv", callback_data='21')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('pick one of the options to get price', reply_markup=reply_markup)

def getResult(name,query):
    with open(data_path) as json_file:
            data = json.load(json_file)
            for p in data['digital_currencies']:
                if(name in p['asset']):
                    query.edit_message_text(str(p))
def button(update, context):
    query = update.callback_query

    
    query.answer()
    if(format(query.data)=='1'):
        getResult("BTC",query)
    elif(format(query.data)=='2'):
        getResult("ETH",query)
    elif(format(query.data)=='3'):
        getResult("XRP",query)

    elif(format(query.data)=='4'):
        getResult("USDT",query)

    elif(format(query.data)=='5'):
        getResult("LINK",query) 

    elif(format(query.data)=='6'):
        getResult("XLM",query)
    elif(format(query.data)=='7'):
        getResult("BCH",query) 

    elif(format(query.data)=='8'):
        getResult("LTC",query)

    elif(format(query.data)=='9'):
        getResult("USDC",query)
    elif(format(query.data)=='10'):
        getResult("EOS",query)
    elif(format(query.data)=='11'):
        getResult("XMR",query)
    elif(format(query.data)=='12'):
        getResult("TRX",query)
    elif(format(query.data)=='13'):
        getResult("XTZ",query)
    elif(format(query.data)=='14'):
        getResult("ZEC",query)
    elif(format(query.data)=='15'):
        getResult("DASH",query)
    elif(format(query.data)=='16'):
        getResult("ETC",query)
    elif(format(query.data)=='17'):
        getResult("DAI",query)
    elif(format(query.data)=='18'):
        getResult("ZRX",query)
    elif(format(query.data)=='19'):
        getResult("OXT",query)
    elif(format(query.data)=='20'):
        getResult("BSV",query)





def help_command(update, context):
    update.message.reply_text("please send /start for start")


def main():
    # get api token from FatherBot in telegram
    updater = Updater("Telegram bot API token", use_context=True)

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler('help', help_command))

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()
