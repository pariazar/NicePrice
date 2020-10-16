#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

"""
Basic example for a bot that uses inline keyboards.
"""
import logging 
import json
import py_compile
import os

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def start(update, context):
    os.system("python updateCost3.py")  

    keyboard = [[InlineKeyboardButton("دلار", callback_data='1'),
                 InlineKeyboardButton("سکه", callback_data='3')],
                 [InlineKeyboardButton("مثقال طلا", callback_data='4'),
                 InlineKeyboardButton(" انس طلا", callback_data='6'),
                 InlineKeyboardButton(" طلا ۱۸", callback_data='5'),
                 InlineKeyboardButton("یورو", callback_data='2'),
                 InlineKeyboardButton("نفت برنت", callback_data='7'),
                 InlineKeyboardButton("بیت کوین", callback_data='8')],
                [InlineKeyboardButton("شاخص بورس", callback_data='9')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('برای دریافت قیمت ریالی گزینه مورد نظر را انتخاب کنید', reply_markup=reply_markup)


def button(update, context):
    query = update.callback_query

    
    query.answer()
    if(format(query.data)=='1'):
        with open('currencies.json') as json_file:
            data = json.load(json_file)
            for p in data['currencies']:
                query.edit_message_text(p['dollar']) 
    elif(format(query.data)=='2'):
        with open('currencies.json') as json_file:
            data = json.load(json_file)
            for p in data['currencies']:
                query.edit_message_text(p['eur']) 
    elif(format(query.data)=='3'):
        with open('currencies.json') as json_file:
            data = json.load(json_file)
            for p in data['currencies']:
                query.edit_message_text(p['coin']) 

    elif(format(query.data)=='4'):
        with open('currencies.json') as json_file:
            data = json.load(json_file)
            for p in data['currencies']:
                query.edit_message_text(p['mes']) 

    elif(format(query.data)=='5'):
        with open('currencies.json') as json_file:
            data = json.load(json_file)
            for p in data['currencies']:
                query.edit_message_text(p['gr']) 

    elif(format(query.data)=='6'):
        with open('currencies.json') as json_file:
            data = json.load(json_file)
            for p in data['currencies']:
                query.edit_message_text(p['ons']) 
    elif(format(query.data)=='7'):
        with open('currencies.json') as json_file:
            data = json.load(json_file)
            for p in data['currencies']:
                query.edit_message_text(p['oil']) 

    elif(format(query.data)=='8'):
        with open('currencies.json') as json_file:
            data = json.load(json_file)
            for p in data['currencies']:
                query.edit_message_text(p['bitcoin']) 

    elif(format(query.data)=='9'):
        with open('currencies.json') as json_file:
            data = json.load(json_file)
            for p in data['currencies']:
                query.edit_message_text(p['bourse']) 





def help_command(update, context):
    update.message.reply_text("از دکمه /start جهت دریافت قیمت ها استفاده کنید")


def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("1348041399:AAFyVhctlfvSnS4oKZ0OpzETGWdTRs3YgrU", use_context=True)

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
