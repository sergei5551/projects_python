from telebot import *
import requests
from random import randint, choice
from bs4 import BeautifulSoup

games = {
    'RPG': 'https://thelastgame.ru/category/rpg/',
    'Драки': 'https://thelastgame.ru/category/fight/'
}

token = '5683949044:AAEHvOuXlFhFsV7yfCYclPJT9sNVYTFC4Fw'
bot = TeleBot(token)

@bot.message_handler(commands=['start'])
def welcome(message):
    text = 'Начало'
    keybord = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=False)
    button1 = types.KeyboardButton('Картинка')
    button2 = types.KeyboardButton('Аудио')
    button3 = types.KeyboardButton('Игра')
    keybord.add(button1, button2, button3)
    bot.send_message(message.chat.id, text, reply_markup=keybord)

@bot.message_handler(commands=['open'])
def send_image(message):
    photo = open('trava.jpg', 'rb')
    bot.send_photo(message.chat.id, photo)


@bot.message_handler(commands=['lissen'])
def send_audio(message):
    audio = open('ss.mp3', 'rb')
    bot.send_audio(message.chat.id, audio)

@bot.message_handler(commands=['game'])
def send_game(message):
    text = 'Жанр?'
    keybord2 = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=False)
    button1 = types.KeyboardButton('RPG')
    button2 = types.KeyboardButton('Драки')
    button3 = types.KeyboardButton('Назад')
    keybord2.add(button1, button2, button3)
    bot.send_message(message.chat.id, text, reply_markup=keybord2)


@bot.message_handler(commands=['ganre'])
def button1_answer(message):
    response = requests.get(games['RPG'] + '/page/' + str(randint(2, 9)) + '/')
    html = BeautifulSoup(response.content, 'lxml')
    znach_html = html.find_all(class_="post-title entry-title")
    znach_random_html = choice(znach_html)
    link = znach_random_html.a['href']
    text = link
    bot.send_message(message.chat.id, text)

def button2_answer(message):
    response = requests.get(games['Драки'] + '/page/' + str(randint(2, 9)) + '/')
    html = BeautifulSoup(response.content, 'lxml')
    znach_html = html.find_all(class_="post-title entry-title")
    znach_random_html = choice(znach_html)
    link = znach_random_html.a['href']
    text = link
    bot.send_message(message.chat.id, text)


@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text == 'Картинка':
        send_image(message)
    elif message.text == 'Аудио':
        send_audio(message)
    elif message.text == 'Игра':
        send_game(message)
    elif message.text == 'RPG':
        button1_answer(message)
    elif message.text == 'Драки':
        button2_answer(message)
    elif message.text == 'Назад':
        welcome(message)
bot.polling()
