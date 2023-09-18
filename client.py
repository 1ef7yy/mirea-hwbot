import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
import config
import databaseParser as dbParser


bot = telebot.TeleBot(config.TOKEN)

subjects = {
    "Матан": "matan",
    "Линал": "linal",
    "Информатика": "compsci",
    "ООП": "oop",
    "История": "history",
    "ОРГ": "org",
    "Русский": "russian",
    "Английский": "english",
    "Физика": "physics",
}

def gen_markup(type_of_request: str):
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    for subject in subjects:
        markup.add(InlineKeyboardButton(subject, callback_data=f'{type_of_request}, {subjects[subject]}'))
    if type_of_request == "GET":
        markup.add(InlineKeyboardButton("Все предметы", callback_data=f'{type_of_request}, all'))
    return markup

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    argLoad = call.data.split(', ')
    if argLoad[0] == "GET":
        bot.send_message(call.message.chat.id, dbParser.getHomework(argLoad))
    if argLoad[0] == "POST":
        bot.send_message(call.message.chat.id, dbParser.addHomework(argLoad))

@bot.message_handler(commands=['start, help'])
def start(message):
    bot.send_message(message.chat.id, "start message")


@bot.message_handler(commands=['add', 'add_hw'])
def add_hw(message):
    bot.send_message(message.chat.id, "Выберите предмет, в который надо добавить дз:", reply_markup=gen_markup(type_of_request="POST"))
    


@bot.message_handler(commands=['get', 'get_hw'])
def get_hw(message):
    bot.send_message(message.chat.id, "Выберите предмет:", reply_markup=gen_markup(type_of_request="GET"))

    
bot.infinity_polling()
