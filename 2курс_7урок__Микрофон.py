'''
import requests
from bs4 import BeautifulSoup
import datetime
date = datetime.datetime.today().strftime('%d/%m/%Y')

url_main = 'https://cbr.ru/scripts/XML_daily.asp'
url_date = f'?date_req={date}'

valuts_id = ['R01235', 'R01239', 'R01335', 'R01355', 'R01135']

def get_exchange_rate(id):
    response = requests.get(url_main + url_date)
    soup = BeautifulSoup(response.content, 'lxml')
    w = soup.find('valute', id=id)
    print(f'{w.nominal.text} {w.find("name").text} стоит {w.value.text} рублей')

for i in valuts_id:
    get_exchange_rate(i)
'''

import pyaudio
import speech_recognition as sr
from random import choice as ch
priv = ['Здравствуй', 'Приветствую, повелитель', 'Не общайся со мной!']
film = ['Мстители: Финал', 'Форрест Гамп', '1+1', 'Зеленая миля', 'Назад в будущее']

def films():
    return ch(film)
def privetstvie():
    return ch(priv)

r = sr.Recognizer()

with sr.Microphone() as source:
    print('Скажи что-нибудь')
    audio = r.listen(source)
    speech = r.recognize_google(audio, language='ru_RU').lower()
print(f'Вы сказали: {speech}\n')


if speech == 'привет':
    print(privetstvie())
if speech == 'фильм':
    print(films())
'''
from pygame import mixer
from gtts import gTTS

filenames = ['golos.txt','pp.txt','ss.txt']

def get_text(filenames): # Читаем текст
    file=open(filenames, 'r', encoding='utf-8')
    speech = file.read()
    return speech
def get_audio(speech, filename): # Создание mp3
    tts = gTTS(text=speech, lang='ru')
    filename = filename.replace('txt', 'mp3')
    tts.save(filename)
for filename in filenames:
    text = get_text(filename)
    get_audio(text, filename)



# Воспроизведение аудиофайла при запуске проги
mixer.init()
mixer.music.load('golos.mp3')
mixer.music.play()
'''



