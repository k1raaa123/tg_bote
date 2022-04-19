import telebot
import inf

bot = telebot.TeleBot(inf.token)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'test':
        bot.send_message(message.from_user.id, message.from_user.id)


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
