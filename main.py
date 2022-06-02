import telebot
import database.db
from database.db import get_timetable, get_days, get_dz
from telebot import types

from aiogram.utils.callback_data import CallbackData

from aiogram.dispatcher.filters import Text

from datetime import datetime, date, time


bot = telebot.TeleBot('5295767643:AAHPejjNlmH-TpSbeHq7jRMIn3qxYgP9Lpc')

def main_menu(m):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)

    markup_items = ["Расписание","Ссылки","Контакты","ДЗ"]

    markup.add(*markup_items)
    markup.add("/start")
    bot.send_message(m.chat.id,
                     'Нажми: ' +
                     '\nКонтакты — для контактов преподователй' +
                     '\nСсылки — для получения полезных ссылок (гугл диски и т.п.) ' +
                     '\nРасписание — для просмотра раписания ' +
                     '\nДЗ — для дз по предметам ',
                     reply_markup=markup)

@bot.message_handler(commands=["start"])
def start(m, res=False):
        bot.send_message(m.chat.id, text="Вас приветсует бот помщник!")
        main_menu(m)

def get_contacts():
    contacts = {
        "Орлова Валерия Львовна" : ("vk.cc/cbcwg8"),
        "Главина Сафия Шамсутдиновна": ("vk.cc/cbczAq"),
        "Волкова Ольга Фёдоровна": ("vk.cc/cbcztP"),
        "Коломойцева Татьяна Васильевна": ("vk.cc/cbczlG"),
        "Папаев Павел Леонидович": ("vk.cc/cbcxbj"),
        "Филиппова Елена Борисовна": ("vk.cc/cbcxkN"),
        "Хохрякова Юлия Владимировна": ("vk.cc/cb5v98"),
        "Конюхов Валерий Юрьевич": ("vk.cc/cb5vbH"),
        "Васецкий Алексей Михайлович": ("vk.cc/cbcy1I","vk.cc/cbcy1I"),
        "Филиппова Елена Борисовна": ("vk.cc/cbcxkN"),
        "Щербинин Максим Юрьевич": ("vk.cc/2VlOWH"),
        "Иванов Святослав": ("vk.cc/cbcx3L"),
        "Красильников Игорь Владимирович": ("vk.cc/cbcwCM")
    }
    return contacts;

def get_fios():
    list = [
        "Орлова Валерия Львовна",
        "Главина Сафия Шамсутдиновна",
        "Волкова Ольга Фёдоровна",
        "Коломойцева Татьяна Васильевна",
        "Папаев Павел Леонидович",
        "Филиппова Елена Борисовна",
        "Хохрякова Юлия Владимировна",
        "Конюхов Валерий Юрьевич",
        "Васецкий Алексей Михайлович",
        "Филиппова Елена Борисовна",
        "Щербинин Максим Юрьевич",
        "Иванов Святослав",
        "Красильников Игорь Владимирович"
        ]
    return list

def get_referenses():
    references = {
        "vk.cc/cbcwg8":"Discord: ОрловаВЛ",
        "vk.cc/cbczAq": "Googdle Drive: папка с работами",
        "vk.cc/cbcztP": "Сайт ВУЗа"
    }
    return references



@bot.message_handler(commands=["contacts"])
def show_contacts(message):

    contacts = get_contacts()
    fios = get_fios()
    i = 0

    keyboard = []

    keyboard.append(telebot.types.InlineKeyboardButton(fios[0], url="https://" + contacts[fios[0]]))
    keyboard.append(telebot.types.InlineKeyboardButton(fios[1], url="https://"+contacts[fios[1]]))
    keyboard.append(telebot.types.InlineKeyboardButton(fios[2], url="https://"+contacts[fios[2]]))
    keyboard.append(telebot.types.InlineKeyboardButton(fios[3], url="https://"+contacts[fios[3]]))
    keyboard.append(telebot.types.InlineKeyboardButton(fios[4], url="https://"+contacts[fios[4]]))
    keyboard.append(telebot.types.InlineKeyboardButton(fios[5], url="https://"+contacts[fios[5]]))
    keyboard.append(telebot.types.InlineKeyboardButton(fios[6], url="https://"+contacts[fios[6]]))


    keyboard_elements = [[element] for element in keyboard]

    markup = telebot.types.InlineKeyboardMarkup(keyboard=keyboard_elements)
    return markup

@bot.message_handler(commands=["referense"])
def show_referense(message):

    contacts = get_contacts()
    fios = get_fios()
    ref = get_referenses()
    i = 0

    keyboard = []

    keyboard.append(telebot.types.InlineKeyboardButton(ref[contacts[fios[0]]], url="https://" + contacts[fios[0]]))
    keyboard.append(telebot.types.InlineKeyboardButton(ref[contacts[fios[1]]], url="https://"+contacts[fios[1]]))
    keyboard.append(telebot.types.InlineKeyboardButton(ref[contacts[fios[2]]], url="https://www.muctr.ru/"))

    keyboard_elements = [[element] for element in keyboard]

    markup = telebot.types.InlineKeyboardMarkup(keyboard=keyboard_elements)
    return markup

@bot.message_handler(commands=["dz"])
def show_dz(message):
    keyboard = telebot.types.InlineKeyboardMarkup()

    keyboard.row(
        telebot.types.InlineKeyboardButton("Вчера", callback_data="dz_pst"),
        telebot.types.InlineKeyboardButton("Сегодня", callback_data="dz_prs"),
        telebot.types.InlineKeyboardButton("Завтра", callback_data="dz_fut")
    )

    return keyboard

@bot.message_handler(commands=["table"])
def show_table(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    days = get_days()

    for day in days:
        keyboard.add(telebot.types.InlineKeyboardButton(day[1], callback_data=f"tbl_{day[0]}"),row_width=5)

    return keyboard

@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.strip() == "Расписание" :
        bot.send_message(message.chat.id, text="Узнать расписание на",reply_markup=show_table(message))
        return
    elif message.text.strip() == "Контакты":
        bot.send_message(message.chat.id, text="Список контактов:", reply_markup=show_contacts(message))
        return
    elif message.text.strip() == "ДЗ":
        bot.send_message(message.chat.id, text="Узнать ДЗ на",reply_markup=show_dz(message))
        return
    elif message.text.strip() == "Ссылки":
        bot.send_message(message.chat.id, text="Полезные ссылки:", reply_markup=show_referense(message))
        return
    else:

        restart = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
        restart.add("/start")
        bot.send_message(
            message.chat.id,
            text="Ваша команда не распознона",
            reply_markup=restart
        )
        return

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    data = call.data
    if data.startswith('tbl_'):
        call_table(call)
    elif data.startswith('dz_'):
        call_dz(call)

def call_table(call):

    msg = ""
    day = call.data[4:]

    table = get_timetable(day)

    str_day = ""

    for row in table:
        msg += f"{row[1]} - {row[2]} : {row[3]} \n"
        str_day = row[0]

    msg = f"Расписание на {str_day}:\n" + msg


    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, msg)
    # bot.send_chat_action(call.message.id,'typing')

def call_dz(call):

    weekday = datetime.weekday(datetime.now())

    if call.data == "dz_pst":
        msg = "Домашнее задание на вчера:\n"
        weekday = (7 + weekday - 1) % 7
    elif call.data == "dz_fut":
        msg = "Домашнее задание на завтра:\n"
        weekday = (weekday + 1) % 7
    else:
        msg = "Домашнее задание на сегодня:\n"

    query_result = get_dz(weekday + 1)

    dz_desc = "\n - Домашнее задание отсутствует\n"

    if (len(query_result) > 0):
        dz_desc = ""
        for row in query_result:
            dz_desc += f"\n - {row[0]}:\n {row[1]}\n"

    msg = msg + dz_desc

    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, msg)


bot.polling(none_stop=True, interval=0)




