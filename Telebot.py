import telebot

# 5347371759:AAFsOamBNe3xX-4GE7NA-gXwGKpEZo0HtvQ

bot = telebot.TeleBot('5347371759:AAFsOamBNe3xX-4GE7NA-gXwGKpEZo0HtvQ')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, 'Привет')

@bot.message_handler(func= lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)
bot.polling()
