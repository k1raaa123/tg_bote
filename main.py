import telebot

bot = telebot.TeleBot('5056881947:AAFwUCuBpIPUoovM0uok5-ptzwmy9kEMpKU')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'll':
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
