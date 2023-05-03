import scraping
import os
import telebot


BOT_TOKEN = ''

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, str(scraping.message_data))





bot.infinity_polling()