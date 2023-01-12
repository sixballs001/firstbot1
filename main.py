import telebot
from telebot import types

from config import TOKEN# импортируем файл config.py в котором лежит переменная токен с ключем токена
# import weather
# city = weather.template_city
from ufa import template_city4
from omsk import template_city3
from novyiurengoi import template_city2
from harasavei import template_city1
from bovanenkovo import template_city
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def any_msg(message):
    keyboard = types.InlineKeyboardMarkup()
    callback_button = types.InlineKeyboardButton(text="Бованенково", callback_data="test")
    callback_button1 = types.InlineKeyboardButton(text="Харасавэй", callback_data="test1")
    callback_button2 = types.InlineKeyboardButton(text="Новый Уренгой", callback_data="test2")
    callback_button3 = types.InlineKeyboardButton(text="Омск", callback_data="test3")
    callback_button4 = types.InlineKeyboardButton(text="Уфа", callback_data="test4")
    #array = ['Hello', 'Goodbye', 'Start', 'Price']
    #keyboard.add(*array)
    #keyboard.add(callback_button3, )
    keyboard.add(callback_button, callback_button1, callback_button3, row_width=2)
    keyboard.row(callback_button2, callback_button4)

    bot.send_message(message.chat.id, "Выберите город:", reply_markup=keyboard)

# @bot.message_handler(content_types=['text'])
# def pogoda(message):
#     if message.text == "Бованенково":
#         bot.send_message(message.from_user.id, city = weather.city)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "test":
            bot.send_message(chat_id=call.message.chat.id, text=template_city)
        elif call.data == "test1":
            bot.send_message(chat_id=call.message.chat.id, text=template_city1)
        elif call.data == "test2":
            bot.send_message(chat_id=call.message.chat.id, text=template_city2)
        elif call.data == "test3":
            bot.send_message(chat_id=call.message.chat.id, text=template_city3)
        elif call.data == "test4":
            bot.send_message(chat_id=call.message.chat.id, text=template_city4)



bot.polling(none_stop=True)