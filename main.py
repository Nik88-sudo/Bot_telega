import telebot

bot = telebot.TeleBot('8192428765:AAGWApGg1wflBCJ9p-p9qdpTNw3GCqqwYbc')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!')
bot.polling(none_stop=True)