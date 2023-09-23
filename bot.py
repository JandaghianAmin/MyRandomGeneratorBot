import os
import random
import telebot

BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=['rnd', 'randome'])
def echo_all(message):
    random_float = random.uniform(1.0, 100.0)  # Generates a random float between 1.0 (inclusive) and 100.0 (exclusive)
    bot.reply_to(message, random_float)    

bot.infinity_polling()





