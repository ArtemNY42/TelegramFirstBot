import telebot
from telebot import types

#main variables
TOKEN = "5988556102:AAEyVc4Qz2FpAAOOboLkMWNqOWSvMVA-5T0"
bot = telebot.TeleBot(TOKEN)
change = ""

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, {message.from_user.first_name} {message.from_user.last_name}! Это тестойвый бот, для помощи нажми на кнопку Help'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    help = types.KeyboardButton('Help')
    markup.add(help)
    bot.send_message(message.chat.id, f'Привет! Это тестовый бот, для помощи нажми на кнопку Help.', reply_markup=markup)

@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Go to website", url = "https://www.youtube.com/"))
    bot.send_message(message.chat.id, 'Go to website', reply_markup=markup)

@bot.message_handler(commands=['help'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    website = types.KeyboardButton('Website')
    start = types.KeyboardButton('Start')
    photo = types.KeyboardButton('Photo')

    markup.add(website, start, photo)
    bot.send_message(message.chat.id, 'All buttons', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == "Photo":
        photo = open('CatPhoto.JPG', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == "Website":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Go to website", url="https://www.youtube.com/"))
        bot.send_message(message.chat.id, 'Go to website', reply_markup=markup)
    elif message.text == "Start":
        mess = f'Привет, {message.from_user.first_name} {message.from_user.last_name}! Это тестойвый бот, для помощи нажми на кнопку Help'
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        website = types.KeyboardButton('Help')
        markup.add(website, start)
        bot.send_message(message.chat.id, mess, reply_markup=markup)
    elif message.text == "Help":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        website = types.KeyboardButton('Website')
        start = types.KeyboardButton('Start')
        photo = types.KeyboardButton('Photo')
        markup.add(website, start, photo)
        bot.send_message(message.chat.id, 'All buttons', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Я тебя не понимаю', parse_mode='html')

bot.polling(none_stop=True)
