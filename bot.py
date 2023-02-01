# бот для телеги ↓↓↓
import telebot

value = ''
old_value = ''

bot = telebot.TeleBot('5843878434:AAGMUiaUkRhntogj7XcaMhP2w7Zr2zEyUUQ')

keyboard = telebot.types.InlineKeyboardMarkup()
keyboard.row(telebot.types.InlineKeyboardButton(' ',  callback_data='no'),
             telebot.types.InlineKeyboardButton('CE',  callback_data='CE'),
             telebot.types.InlineKeyboardButton('←', callback_data='←'),
             telebot.types.InlineKeyboardButton('/',  callback_data='/'))

keyboard.row(telebot.types.InlineKeyboardButton('7',  callback_data='7'),
             telebot.types.InlineKeyboardButton('8',  callback_data='8'),
             telebot.types.InlineKeyboardButton('9',  callback_data='9'),
             telebot.types.InlineKeyboardButton('*',  callback_data='*'))

keyboard.row(telebot.types.InlineKeyboardButton('4',  callback_data='4'),
             telebot.types.InlineKeyboardButton('5',  callback_data='5'),
             telebot.types.InlineKeyboardButton('6',  callback_data='6'),
             telebot.types.InlineKeyboardButton('-',  callback_data='-'))

keyboard.row(telebot.types.InlineKeyboardButton('1',  callback_data='1'),
             telebot.types.InlineKeyboardButton('2',  callback_data='2'),
             telebot.types.InlineKeyboardButton('3',  callback_data='3'),
             telebot.types.InlineKeyboardButton('+',  callback_data='+'))

keyboard.row(telebot.types.InlineKeyboardButton(' ',  callback_data='no'),
             telebot.types.InlineKeyboardButton('0',  callback_data='0'),
             telebot.types.InlineKeyboardButton(',',  callback_data='.'),
             telebot.types.InlineKeyboardButton('=',  callback_data='='))


@bot.message_handler(commands=['start', 'calculater'])
def get_message(message):
    global value
    if value == '':
        bot.send_message(message.from_user.id, '0', reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id, value, reply_markup=keyboard)
    user_full_name = message.from_user.full_name
    main_photo = open('images/main_logo.png', 'rb')
    bot.send_photo(message.from_user.id, main_photo)
    bot.send_message(message.from_user.id, f"👋 Привет, {user_full_name}!\n\nДобро пожаловать в моего RT бота!\n\n"
                                           f"Он создан для домашнего задания к уроку 9 по Python!\n\n"
                                           f"Для начала работы с ботом, достаточно прописать в чат: /start")
    bot.send_message(message.from_user.id, "Для начала вычислений начните вводить число.\n", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_func(query):
    global value, old_value
    data = query.data

    if data == 'no':
        pass
    elif data == 'CE':
        value = ''
    elif data == '←':
        if value != '':
            value = value[:len(value)-1]
    elif data == '=':
        value = str(eval(value))
    else:
        value += data

    if (value != old_value and value != '') or ( '0' != old_value and value == ''):
        if value == '':
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text='0', reply_markup=keyboard)
            old_value = '0'
        else:
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text=value, reply_markup=keyboard)
            old_value = value

    if value == 'Ошибка!': value = ''

bot.polling(none_stop=False, interval=0)