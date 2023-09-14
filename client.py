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
    if type_of_request == "GET":
        for subject in subjects:
            markup.add(InlineKeyboardButton(subject, callback_data=f'{subjects[subject]}, {type_of_request}'))
    elif type_of_request == "POST":
        for subject in subjects:
            markup.add(InlineKeyboardButton(subject, callback_data=f'{subjects[subject]}, {type_of_request}'))
    return markup

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    bot.answer_callback_query(call.id, dbParser.getHomework(call.data))
    print(call)


@bot.message_handler(commands=['start, help'])
def start(message):
    bot.send_message(message.chat.id, "start message")


@bot.message_handler(commands=['add', 'add_hw'])
def add_hw(message):
    bot.send_message(message.chat.id, "Выберите предмет, в который надо добавить дз:", reply_markup=gen_markup("POST"))
    


@bot.message_handler(commands=['get', 'get_hw'])
def get_hw(message):
    bot.send_message(message.chat.id, "Выберите предмет:", reply_markup=gen_markup("GET"))

    
bot.infinity_polling()