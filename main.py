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

#Создадим функции для всех уровней:
def easy_reply(message):
    if message.text == 'Сдаюсь':
        return ('Ты проиграл!')
    global main_dict
    global difficulty_dict
    global current_dict
    global last_letter
    city = message.text
    if last_letter != "" and city[0] != last_letter:
        return "Необходимо назвать город, начинающийся на букву " + '"' + last_letter + '"'
    if city[0] not in main_dict or city not in main_dict[city[0]]:
        return "Я такого города не знаю"
    if city[0] not in current_dict or city not in current_dict[city[0]]:
        return "Этот город уже был использован"
    current_dict[city[0]].pop(city)
    difficulty_dict[city[0]] -= main_dict[city[0]][city]
    if city[-1] in "ёъыь":
        letter = city[-2].capitalize()
    else:
        letter = city[-1].capitalize()
    if letter not in current_dict or len(current_dict[letter]) == 0:
        return ('Ты выиграл!')
    good_cities = set()
    for key_city, value_dif in current_dict[letter].items():
        if key_city[-1] in "ёъыь":
            current_last_letter = key_city[-2].capitalize()
        else:
            current_last_letter = key_city[-1].capitalize()
        good_cities.add((key_city, value_dif, difficulty_dict[current_last_letter]))
    city_return = sorted(good_cities, key=lambda x: (-x[1], x[2]))[-1][0]
    if city_return[-1] in "ёъыь":
        last_letter = city_return[-2].capitalize()
    else:
        last_letter = city_return[-1].capitalize()

    difficulty_dict[last_letter] -= current_dict[city_return[0]][city_return]
    current_dict[city_return[0]].pop(city_return)

    return city_return

def medium_reply(message):
    if message.text == 'Сдаюсь':
        return ('Ты проиграл!')
    global main_dict
    global difficulty_dict
    global current_dict
    global last_letter
    city = message.text
    if last_letter != "" and city[0] != last_letter:
        return "Необходимо назвать город, начинающийся на букву " + '"' + last_letter + '"'
    if city[0] not in main_dict or city not in main_dict[city[0]]:
        return "Я такого города не знаю"
    if city[0] not in current_dict or city not in current_dict[city[0]]:
        return "Этот город уже был использован"
    current_dict[city[0]].pop(city)
    difficulty_dict[city[0]] -= main_dict[city[0]][city]
    if city[-1] in "ёъыь":
        letter = city[-2].capitalize()
    else:
        letter = city[-1].capitalize()
    if letter not in current_dict:
        return "Ты выиграл!"
    good_cities = set()
    for key_city, value_dif in current_dict[letter].items():
        if key_city[-1] in "ёъыь":
            current_last_letter = key_city[-2].capitalize()
        else:
            current_last_letter = key_city[-1].capitalize()
        good_cities.add((key_city, value_dif, difficulty_dict[current_last_letter]))
    city_return = sorted(good_cities, key=lambda x: (-x[1], x[2]))[len(good_cities) // 2][0]
    if city_return[-1] in "ёъыь":
        last_letter = city_return[-2].capitalize()
    else:
        last_letter = city_return[-1].capitalize()
    difficulty_dict[last_letter] -= current_dict[city_return[0]][city_return]
    current_dict[city_return[0]].pop(city_return)
    return city_return


def hard_reply(message):
    if message.text == 'Сдаюсь':
        return ('Ты проиграл!')
    global main_dict
    global difficulty_dict
    global current_dict
    global last_letter
    city = message.text
    if last_letter != "" and city[0] != last_letter:
        return "Необходимо назвать город, начинающийся на букву " + '"' + last_letter + '"'
    if city[0] not in main_dict or city not in main_dict[city[0]]:
        return "Я такого города не знаю"
    if city[0] not in current_dict or city not in current_dict[city[0]]:
        return "Этот город уже был использован"
    current_dict[city[0]].pop(city)
    difficulty_dict[city[0]] -= main_dict[city[0]][city]
    if city[-1] in "ёъыь":
        letter = city[-2].capitalize()
    else:
        letter = city[-1].capitalize()
    if letter not in current_dict:
        return "Ты выиграл!"
    good_cities = set()
    for key_city, value_dif in current_dict[letter].items():
        if key_city[-1] in "ёъыь":
            current_last_letter = key_city[-2].capitalize()
        else:
            current_last_letter = key_city[-1].capitalize()
        good_cities.add((key_city, value_dif, difficulty_dict[current_last_letter]))
    city_return = sorted(good_cities, key=lambda x: (-x[1], x[2]))[0][0]
    if city_return[-1] in "ёъыь":
        last_letter = city_return[-2].capitalize()
    else:
        last_letter = city_return[-1].capitalize()
    difficulty_dict[last_letter] -= current_dict[city_return[0]][city_return]
    current_dict[city_return[0]].pop(city_return)
    return city_return

#

#def easy_game(message):
#        bot.send_message(message.chat.id, easy_reply(message))


def callback_easy_game(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Сдаюсь')
    markup.row(btn1)
    bot.send_message(message.chat.id, easy_reply(message), reply_markup=markup)


    if easy_reply(message) != 'Ты выиграл!' and easy_reply(message) != 'Ты проиграл!':
        bot.register_next_step_handler(message, callback_easy_game)

    elif easy_reply(message) == 'Ты выиграл!' or easy_reply(message) == 'Ты проиграл!':
        markup2 = types.ReplyKeyboardMarkup()
        btn = types.KeyboardButton('Давай сыграем!')
        markup2.row(btn)
        bot.send_message(message.chat.id, 'Если хочешь сыграть ещё, напиши "Давай сыграем!"', reply_markup=markup2)


def callback_medium_game(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Сдаюсь')
    markup.row(btn1)
    bot.send_message(message.chat.id, medium_reply(message), reply_markup=markup)

    markup2 = types.ReplyKeyboardMarkup()
    btn = types.KeyboardButton('Давай сыграем!')
    markup2.row(btn)

    if medium_reply(message) != 'Ты проиграл!' and medium_reply(message) != 'Ты выиграл!':
        bot.register_next_step_handler(message, callback_medium_game)

    elif medium_reply(message) == 'Ты проиграл!' or medium_reply(message) == 'Ты выиграл!':
        markup2 = types.ReplyKeyboardMarkup()
        btn = types.KeyboardButton('Давай сыграем!')
        markup2.row(btn)
        bot.send_message(message.chat.id, 'Если хочешь сыграть ещё, напиши "Давай сыграем!"', reply_markup=markup2)


def callback_hard_game(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Сдаюсь')
    markup.row(btn1)
    bot.send_message(message.chat.id, hard_reply(message), reply_markup=markup)

    markup2 = types.ReplyKeyboardMarkup()
    btn = types.KeyboardButton('Давай сыграем!')
    markup2.row(btn)

    if hard_reply(message) != 'Ты проиграл!' and hard_reply(message) != 'Ты выиграл!':
        bot.register_next_step_handler(message, callback_hard_game)

    elif hard_reply(message) == 'Ты проиграл!' or hard_reply(message) == 'Ты выиграл!':
        markup2 = types.ReplyKeyboardMarkup()
        btn = types.KeyboardButton('Давай сыграем!')
        markup2.row(btn)
        bot.send_message(message.chat.id, 'Если хочешь сыграть ещё, напиши "Давай сыграем!"', reply_markup=markup2)


#Здесь будет сам код, когда мы получаем уровень сложности

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    global main_dict
    global current_dict
    global difficulty_dict
    global last_letter
    last_letter = ""
    current_dict = {}
    difficulty_dict = {}
    for let, value in main_dict.items():
        if let not in current_dict:
            current_dict[let] = {}
            difficulty_dict[let] = 0
        for city, dif in value.items():
            current_dict[let][city] = main_dict[let][city]
            difficulty_dict[let] += main_dict[let][city]
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




main_dict = {}
difficulty_dict = {}
current_dict = {}
last_letter = ""
with open('cities.txt', 'r', encoding='utf-8') as fin:
    line = fin.readline()
    line = line.replace('\ufeff', '')
    while line != '':
        new_line = line.strip().split(" ")
        city_name = new_line[0]
        for el in new_line[1:len(new_line) - 1]:
            city_name += " " + el
        city_difficulty = int(new_line[-1])
        if city_name[0] not in main_dict:
            main_dict[city_name[0]] = {}
        main_dict[city_name[0]][city_name] = city_difficulty
        line = fin.readline()


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
        #webbrowser.open('https://github.com/')
        bot.send_message(message.chat.id, 'https://github.com/oakobzeva/Telegram-Bot?tab=readme-ov-file#telegram-bot')
    else:
        bot.reply_to(message, 'Что-то я не понял...')







bot.polling(none_stop=True)




