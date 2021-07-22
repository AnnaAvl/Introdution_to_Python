import telebot
from telebot import types
import random

# Список слов для игры
arr = ['арбуз', 'машина', 'банан', 'дерево', 'кукла',
       'майка', 'дверь', 'солнце', 'картина', 'колесо',
       'велосипед', 'ручка', 'молния', 'друг', 'стоянка']

# Строка для проверки, содержащая буквы, которые могут быть названы
abc = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

# Создаем бота
bot = telebot.TeleBot("1841133840:AAFDK_I2ZYoxpFh7pv5GNXA_Q46DQmnLslE")

# Создаем конпку для старта
markup_start = types.ReplyKeyboardMarkup(one_time_keyboard=True)
btn_start = types.InlineKeyboardButton('Старт')
markup_start.add(btn_start)

# Создаем конпку для выхода
markup_end = types.ReplyKeyboardMarkup(one_time_keyboard=True)
btn_end = types.InlineKeyboardButton('Выйти')
markup_end.add(btn_end)

# Создаем конпки для ответа на вопрос, хочет ли игрок продолжить игру
markup_q_a = types.ReplyKeyboardMarkup(one_time_keyboard=True)
btn_yes = types.InlineKeyboardButton('Да')
btn_no = types.InlineKeyboardButton('Нет')
markup_q_a.add(btn_yes, btn_no)


@bot.message_handler(content_types=['text'])
def begin(message):
    # Бот выводит сообщение о начале игры и кнопку для старта
    bot.send_message(message.from_user.id, 'Привет! Для начала игры, нажми на кнопку или напиши команду "старт"',
                     reply_markup=markup_start)
    # Переходим к следующей фуннкции, после ответа пользователя
    bot.register_next_step_handler(message, start)


def start(message):
    # Если пользователь ошибся при вводе команды, бот переспросит его
    if str(message.text).lower() != 'старт':
        bot.send_message(message.from_user.id, 'Ничего не понимаю. Введи команду "старт"')
        # Переходим к началу функции для проверки корректности ввода
        bot.register_next_step_handler(message, start)
    else:
        # Иначе, бот выводит сообщение о начале игры,
        # предлагая закончить игру преждевременно с помощью кнопки или команды
        bot.send_message(message.from_user.id,
                         'Игра началась! Если хочешь ее закончить нажми на кнопку или напиши команду "выйти"')
        # Выбираем рандомное слово из списка
        word = random.choice(arr).lower()
        # Загаданное слово шифруем символами "*"
        guess_word = '*' * len(word)
        # Число ошибок
        miss = 10
        # Строка, в которую будем записывать названные буквы
        letters = ''
        # Бот загадывает слово, просит пользователя отгадать его и выводит кнопку для выхода из игры
        bot.send_message(message.from_user.id, 'Я загадал слово. Попробуй его отгадать! Назови букву\n' + guess_word,
                         reply_markup=markup_end)
        # Переходим к циклу игры
        bot.register_next_step_handler(message, game, word, guess_word, miss, letters)


def game(message, word, guess_word, miss, letters):
    # Если пользователь хочет преждевременно окончить игру, бот оповещает о ее окончании
    # и выводит загаданное слово, удаляем кнопки, если ими не воспользовались
    if message.text.lower() == 'выйти':
        bot.send_message(message.from_user.id, 'Игра окончена. Загаданное слово: ' + word,
                         allow_sending_without_reply=True, reply_markup=types.ReplyKeyboardRemove())
        return
    else:
        # Если введено более/менее одной буквы, она не содержится в русском алфавите
        # или она уже была названа, просим пользователя ввести другую букву.
        if len(list(message.text.lower())) != 1 or abc.find(message.text.lower()) == -1 or letters.find(
                message.text.lower()) != -1:
            bot.send_message(message.from_user.id, 'Назови другую букву', allow_sending_without_reply=True)
            # Переходим к началу функции для проверки корректности ввода
            bot.register_next_step_handler(message, game, word, guess_word, miss, letters)
        else:
            # Если буква прошла все проверки, присваиваем ее переменной
            letter = message.text.lower()
            # Если список букв пуст, добавляем букву.
            # Если буквы уже имеются, добавляем их через запятую,
            # для корректного вывода пользователю
            if letters == '':
                letters += letter
            else:
                letters = letters + ', ' + letter
            # Если загаданное слово не содержит букву, которую назвал
            # пользователь, отнимаем одну жизнь, добавляем букву в список
            # названных, выводим сообщение
            if word.find(letter) == -1:
                miss -= 1
                if miss > 0:
                    # Сообщение об ошибке, если у игрока остались жизни
                    bot.send_message(message.from_user.id, 'Неверно :(\nОсталось ошибок: ' + str(
                        miss) + '\nНазванные буквы: ' + letters + '\n' + guess_word + '\nПопробуй назвать другую букву')
                else:
                    # Сообщение о проигрыше, если жизни закончились, выводим клавиатуру для ответа на вопрос.
                    # Сообщение не требует ответа, т.к. потребуется ответ от пользователя, при переходе к функции
                    bot.send_message(message.from_user.id,
                                     'Ты проиграл :( Загаданное слово: ' + word + '. Хочешь сыграть еще раз? (Да/Нет)',
                                     allow_sending_without_reply=True, reply_markup=markup_q_a)
                    bot.register_next_step_handler(message, end_of_game)
            # Если названная буква есть в слове
            else:
                index = -1
                # Пока в слове, которое видит игрок, все нужные символы "*"
                # не будут заменены названной буквой, определяем в загаданном
                # слове индексы буквы и в слове игрока символы "*" с данным
                # индексом заменяем на букву
                while guess_word.count(letter) != word.count(letter):
                    index = word.find(letter, index + 1)
                    guess_word = guess_word[:index] + letter + guess_word[index + 1:]
                if word != guess_word:
                    # Если слово еще не угадано, выводим пользователю всю нужную информацию
                    bot.send_message(message.from_user.id, '\nОсталось ошибок: ' + str(
                        miss) + '\nНазванные буквы: ' + letters + '\n' + guess_word + '\nНазови еще одну букву')
                else:
                    # Сообщение о выигрыше, если слово отгадано, выводим клавиатуру для ответа на вопрос.
                    # Сообщение не требует ответа, т.к. потребуется ответ от пользователя, при переходе к функции
                    bot.send_message(message.from_user.id, 'Загаданное слово: '
                                     + guess_word + '\nТы выиграл! Хочешь сыграть еще раз?(Да/Нет)',
                                     allow_sending_without_reply=True, reply_markup=markup_q_a)
                    bot.register_next_step_handler(message, end_of_game)
            # Если слово еще не угадано, продолжаем спрашивать у пользователя буквы
            if miss > 0 and word != guess_word:
                bot.register_next_step_handler(message, game, word, guess_word, miss, letters)


def end_of_game(message):
    if message.text.lower() == 'да':
        # Если пользователь хочет продолжить игру, бот выводит сообщение о новой игре.
        # Сообщение не требует ответа, т.к. потребуется ответ от пользователя, при переходе к функции
        bot.send_message(message.from_user.id, 'Новая игра', allow_sending_without_reply=True)
        bot.send_message(message.from_user.id, 'Для начала игры, нажми на кнопку или напиши команду "старт"',
                         allow_sending_without_reply=True, reply_markup=markup_start)
        bot.register_next_step_handler(message, start)
    elif message.text.lower() == 'нет':
        # Если пользователь не хочет продолжить игру, выходим
        bot.send_message(message.from_user.id, 'Игра окончена', allow_sending_without_reply=True,
                         reply_markup=types.ReplyKeyboardRemove())
        return
    else:
        # При некорректном вводе, бот переспрашавет, переходя к началу функции, для проверки ответа
        bot.send_message(message.from_user.id, 'Хм... Что-то я ничего не понял. Ты хочешь сыграть еще раз?',
                         allow_sending_without_reply=True)
        bot.register_next_step_handler(message, end_of_game)


bot.polling()
