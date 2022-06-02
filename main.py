import telebot
import database.db
from database.db import get_timetable, get_days
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

def get_dz():
    dz = {
        "ПН":[
            "Теория вероятностей и мат. статистика	семинар",
            "Физическая химия	семинар",
            "Английский язык	семинар"
        ],
        "ВТ": [
            "Веб-программирование	лаба",
            "Численные методы в среде MATLAB	лаба"
        ],
        "СР": [

        ],
        "ЧТ": [
            "Технологии программирования	лаба дедлайн 25.02"
        ],
        "ПТ": [
            "ЭлФКиС   тест",
            "Архитектура информационных систем	лаба3 дедлайн 25.02"
        ],
        "СБ": [

        ],
        "ВС": [

        ]
    }
    return dz

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
    dz = get_dz()

    dayofweek = ["ПН","ВТ","СР","ЧТ","ПТ","СБ","ВС"]

    weekday = dayofweek[datetime.weekday(datetime.now())]

    msq = "Домашнее задание на сегодня:\n"

    if (len(dz[weekday]) == 0):
        msq += "Отсутствует"
    else:
        for string in dz[weekday]:
            msq += " - " + string + "\n"

    bot.send_message(message.chat.id, text=msq)

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
        show_dz(message)
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


@bot.callback_query_handler(Text(startswith="tbl_"))
def callback_handler(call):

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




bot.polling(none_stop=True, interval=0)




