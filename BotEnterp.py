# -*- coding: cp1251 -*-
import telebot
from telebot import apihelper
import apiai, json
from apiai.apiai import ApiAI
import os

apihelper.proxy = {'https':'socks5://mtpro_xyz:mtpro_xyz_bot@exp1.s5overss.mtpro.xyz:39610'}

API_TOKEN = os.environ["API_TOKEN"]
bot = telebot.TeleBot(API_TOKEN)
bot.remove_webhook()

AItok = os.environ["AItok"]
'''@bot.message_handler(commands=['start'])
def startCommand(message):
    bot.send_message(chat_id=message.chat.id, text='Lets get started!')'''
@bot.message_handler(func=lambda message: True)
def textMessage(message):
    request = apiai.ApiAI(AItok).text_request()
    request.lang = 'eng'
    request.session_id = 'BotTalk'
    request.query = message.text
    responseJson = json.loads(request.getresponse().read().decode('utf-8'))
    response = responseJson['result']['fulfillment']['speech']
    if response:
        bot.send_message(chat_id=message.chat.id, text=response)
    else:
        bot.send_message(chat_id=message.chat.id, text='I dont understand you')
#bot.send_message(chat_id=message.chat.id, text=message.text)

bot.polling(none_stop=True, timeout=123)
