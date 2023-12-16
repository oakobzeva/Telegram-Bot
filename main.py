import numpy
import telebot
from telebot import types
import webbrowser

bot = telebot.TeleBot('6340729476:AAHKa8A8rk0lgGAofeHhJowEmUYuh3Cqa30')


@bot.message_handler(commands=['start'])
def beginning(message):
    first_markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Давай сыграем!')
    btn2 = types.KeyboardButton('Страница проекта на Github')
    btn3 = types.KeyboardButton('Информация про создателей')
    first_markup.row(btn1)
    first_markup.row(btn2, btn3)
    bot.send_message(message.chat.id, f'<b>Здравствуй, {message.from_user.first_name} {message.from_user.last_name}!</b> Ну что, сыграем в города?', parse_mode='html', reply_markup=first_markup)
#Это вступительное сообщение, которое отправляется после команды старт


@bot.message_handler()
def play(message):
    if message.text.lower() == 'давай сыграем!':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Лёгкий', callback_data='easy')
        btn2 = types.InlineKeyboardButton('Средний', callback_data='medium')
        btn3 = types.InlineKeyboardButton('Сложный', callback_data='hard')
        markup.row(btn1, btn2, btn3)
        bot.reply_to(message, 'Вызов принят! Выбери уровень сложности.', reply_markup=markup)
    elif message.text.lower() == 'сдаюсь':
        bot.reply_to(message, 'Ты проиграл!') #Если пользователь сдаётся
    elif message.text.lower() == 'привет':
        first_markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Давай сыграем!')
        btn2 = types.KeyboardButton('Страница проекта на Github')
        btn3 = types.KeyboardButton('Информация про создателей')
        first_markup.row(btn1)
        first_markup.row(btn2, btn3)
        bot.send_message(message.chat.id, f'<b>Здравствуй, {message.from_user.first_name} {message.from_user.last_name}!</b> Ну что, сыграем в города?', parse_mode='html', reply_markup=first_markup)
    elif message.text.lower() == 'информация про создателей':
        bot.send_message(message.chat.id, 'Создатели: Кобзева Ольга, группа БМТ213, Нусратуллина Марьям Айратовна, группа БМТ213')
    elif message.text.lower() == 'страница проекта на github':
        bot.send_message(message.chat.id, 'https://github.com/')
        #webbrowser.open('https://github.com/')
    else:
        bot.reply_to(message, 'Что-то я не понял...')

#Создадим функции для всех уровней:
def easy_reply(message):
    if message.text == 'Сдаюсь':
        return ('Ты проиграл! Если хочешь сыграть ещё, напиши "Давай сыграем!"')
    global main_dict
    global cities_all
    if message.text not in cities_all:
        return "Я такого города не знаю"
    for elem in main_dict[message.text[0]]:
        if elem[0] == message.text:
            main_dict[message.text[0]].remove(elem)
            break
    else:
        return "Этот город уже был использован"
    last_letter = message.text[-1].capitalize()
    if message.text[-1] in "ёъыь":
        last_letter = message.text[-2].capitalize()
    if last_letter not in main_dict:
        return "Ты выиграл"
    good_cities = main_dict[last_letter]
    city_return = sorted(good_cities, key=lambda x: x[1], reverse=True)[0][0]
    for elem in main_dict[city_return[0]]:
        if elem[0] == city_return:
            main_dict[city_return[0]].remove(elem)
            break
    return city_return

def medium_reply(message):
    if message.text == 'Сдаюсь':
        return ('Ты проиграл! Если хочешь сыграть ещё, напиши "Давай сыграем!"')
    global main_dict
    if message.text not in cities_all:
        return "Я такого города не знаю"
    for elem in main_dict[message.text[0]]:
        if elem[0] == message.text:
            main_dict[message.text[0]].remove(elem)
            break
    else:
        return "Этот город уже был использован"
    good_cities = main_dict[message.text[-1].capitalize()]
    return sorted(good_cities, key=lambda x: x[1])[len(good_cities) // 2][0]


def hard_reply(message):
    if message.text == 'Сдаюсь':
        return ('Ты проиграл! Если хочешь сыграть ещё, напиши "Давай сыграем!"')
    global main_dict
    if message.text not in cities_all:
        return "Я такого города не знаю"
    for elem in main_dict[message.text[0]]:
        if elem[0] == message.text:
            main_dict[message.text[0]].remove(elem)
            break
    else:
        return "Этот город уже был использован"
    good_cities = main_dict[message.text[-1].capitalize()]
    return sorted(good_cities, key=lambda x: x[1])[0][0]

#

#def easy_game(message):
#        bot.send_message(message.chat.id, easy_reply(message))


def callback_easy_game(message):
    if easy_reply(message) != 'Ты проиграл! Если хочешь сыграть ещё, напиши "Давай сыграем!"' and easy_reply(message) != 'Ты выиграл!':
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Сдаюсь')
        markup.row(btn1)
        bot.send_message(message.chat.id, easy_reply(message), reply_markup=markup)
        bot.register_next_step_handler(message, callback_easy_game)

    else:
        markup2 = types.ReplyKeyboardMarkup()
        btn = types.KeyboardButton('Давай сыграем!')
        markup2.row(btn)
        bot.send_message(message.chat.id, easy_reply(message), reply_markup=markup2)
        


def callback_medium_game(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Сдаюсь')
    markup.row(btn1)

    bot.send_message(message.chat.id, medium_reply(message), reply_markup=markup)
    if medium_reply(message) != 'Ты проиграл! Если хочешь сыграть ещё, напиши "Давай сыграем!"':
        bot.register_next_step_handler(message, callback_medium_game)

def callback_hard_game(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Сдаюсь')
    markup.row(btn1)

    bot.send_message(message.chat.id, hard_reply(message), reply_markup=markup)
    if hard_reply(message) != 'Ты проиграл! Если хочешь сыграть ещё, напиши "Давай сыграем!"':
        bot.register_next_step_handler(message, callback_hard_game)




#Здесь будет сам код, когда мы получаем уровень сложности

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    with open('cities.txt', 'r', encoding='utf-8') as fin:
        line = fin.readline()
        line = line.replace('\ufeff', '')
        global main_dict
        global cities_all
        main_dict = {}
        cities_all = set()
        cities_non_used = set()
        while line != '':
            new_line = line.strip().split(" ")
            city_name = new_line[0]
            for el in new_line[1:len(new_line) - 1]:
                city_name += " " + el
            cities_all.add(city_name)
            city_difficulty = int(new_line[-1])
            if city_name[0] not in main_dict:
                main_dict[city_name[0]] = set()
            main_dict[city_name[0]].add((city_name, city_difficulty))
            line = fin.readline()

    if callback.data == 'easy':
        bot.send_message(callback.message.chat.id, 'Ты выбираешь лёгкий уровень. Первый ход твой! Если признаешь поражение, напиши "Сдаюсь"')
        bot.register_next_step_handler(callback.message, callback_easy_game)

    if callback.data == 'medium':
        bot.send_message(callback.message.chat.id,
                         'Ты выбираешь средний уровень. Первый ход твой! Если признаешь поражение, напиши "Сдаюсь"')
        bot.register_next_step_handler(callback.message, callback_medium_game)

    if callback.data == 'hard':
        bot.send_message(callback.message.chat.id,
                         'Ты выбираешь сложный уровень. Первый ход твой! Если признаешь поражение, напиши "Сдаюсь"')
        bot.register_next_step_handler(callback.message, callback_hard_game)




bot.polling(none_stop=True)
cities_all = set()
main_dict = {}











