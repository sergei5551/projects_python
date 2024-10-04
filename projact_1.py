# PyInstaller
from random import choice, randint
games = {
    'RPG': 'https://thelastgame.ru/category/rpg/',
    'Аркады': 'https://thelastgame.ru/category/arcade/',
    'Гонки': 'https://thelastgame.ru/category/racing/',
    'Драки': 'https://thelastgame.ru/category/fight/',
    'Квесты': 'https://thelastgame.ru/category/quest/',
    'Логические': 'https://thelastgame.ru/category/logic/',
    'Приключения': 'https://thelastgame.ru/category/adventure/',
    'Симуляторы': 'https://thelastgame.ru/category/simulator/',
    'Спорт': 'https://thelastgame.ru/category/sport/',
    'Стратегии': 'https://thelastgame.ru/category/strategy/',
    'Хоррор': 'https://thelastgame.ru/category/horror/',
    'Шутер': 'https://thelastgame.ru/category/shooter/',
    'Экшн': 'https://thelastgame.ru/category/action/',
}
#class="post-title entry-title"
from tkinter import *
import requests
from bs4 import BeautifulSoup

def buttons(texts, place_x, place_y):
    b1 = Button(text=texts, font=('Courier New', 45), bg='#999998', command=lambda: (
        # добыча ссылки с помощью парсинга
        response := requests.get((games[texts])+'/page/'+str(randint(2, 9))+'/'), #ДобовлениеСтрокиДляПолучениРазнойСтраницы
        html := BeautifulSoup(response.content, 'lxml'),
        znach_html := html.find_all(class_="post-title entry-title"),
        znach_random_html := choice(znach_html),
        link := znach_random_html.a['href'],
        title := znach_random_html.a['title'],

        # создание окна с текстом и ссылкой
        window_2 := Tk(),
        window_2.title('Твоя игра'),
        window_2.geometry('700x700'),
        window_2.resizable(width=False, height=False),

        text := Text(window_2,width=30, height=7, font=('Courier New', 25), wrap=WORD, fg='#992994'),
        text.place(x=50, y=0),
        text.insert('1.0', f'Название: {title}'),
        text.insert('2.0', f'\n\nСсылка: {link}'),
        b := Button(window_2, text='Копировать',width=10, font=('Courier New', 45), bg='#999998'),
        b.place(x=170, y=300)

        )


        )
    b1.place(x=place_x, y=place_y)
# Создания окна приложения
window = Tk()
window.title('Поиск игр')
window.geometry('1200x850')
window.resizable(width=False, height=False)

label = Label(text='Какой жанр игры?', font=('TamesNeuRoman', 50), bg='#999999')
label.place(x=280, y=20)

buttons('RPG', 40,120)
buttons('Аркады', 780,120)
buttons('Гонки', 40,240)
buttons('Драки', 780,240)
buttons('Квесты', 40,360)
buttons('Логические', 780,360)
buttons('Приключения', 40,480)
buttons('Симуляторы', 780,480)
buttons('Спорт', 40,600)
buttons('Стратегии', 780,600)
buttons('Хоррор', 40,720)
buttons('Шутер', 780,720)
buttons('Экшн', 425,120)


window.mainloop()
