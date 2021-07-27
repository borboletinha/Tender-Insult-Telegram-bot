import telebot
from settings import TOKEN

bot = telebot.TeleBot(TOKEN)

name = ''

@bot.message_handler(content_types=['text'])

def get_messages(message):

    def get_name(message):
        global name
        name = message.text
        
    match1 = re.fullmatch(r'.*[Пп]рив.*', message.text)
    match2 = re.fullmatch(r'.*[Хх]ай.*', message.text)
    match3 = re.fullmatch(r'.*[Зз]драв.*', message.text)
    
    if message.text == '/help':
        bot.send_message(message.from_user.id, 'Мы сами нуждаемся в помощи')
    elif message.text == '/start':
        bot.send_message(message.from_user.id, 'И тебе не хворать')
    elif match1 or match2 or match3:
        bot.send_message(message.from_user.id, 'Здоровались уже')
    elif message.text == '/insult':
        bot.send_message(message.from_user.id, 'Как тебя зовут?')
        bot.register_next_step_handler(message, get_insult)
    else:
        (bot.send_message(message.from_user.id, 'Мы не понимаем, мы тупи. '
                                                'Единственное, что мы знаем, - примитивные оскорбления, '
                                                'лишенные даже намека на элегантность. Вот напиши нам /insult'))

def get_insult(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, name + ', ты жопа')


bot.polling(none_stop=True, interval=0)
