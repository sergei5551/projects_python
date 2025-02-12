from tkinter import * ; from bs4 import BeautifulSoup
import requests, datetime

def get_exchange_rate(id):
    response = requests.get(url_main)
    soup = BeautifulSoup(response.content, 'xml')
    val = soup.find('Valute', ID=id)
    '''
    # Поиск id валюты
    s = soup.find_all('Valute')
    for i in s:
        if i.Name.text.count('иен'):
            print(i)
    '''

    return val.Value.text
def next():
    if label_usd['text'] ==(f'Доллары\n$--{get_exchange_rate("R01235")}₽') and\
        label_eur['text'] ==(f'Евро\n€--{get_exchange_rate("R01239")}₽') and\
        label_yuan['text'] ==(f'Юань\n¥--{get_exchange_rate("R01375")}₽'):

        label_usd.config(text= f'Австр. доллар\nA$--{get_exchange_rate("R01010")}₽')
        label_eur.config(text=f'Швейц. франки\n₣--{get_exchange_rate("R01775")}₽')
        label_yuan.config(text=f'Японская иена\n¥--{get_exchange_rate("R01820")}₽')

    else:
        label_usd.config(text= f'Доллары\n$--{get_exchange_rate("R01235")}₽')
        label_eur.config(text=f'Евро\n€--{get_exchange_rate("R01239")}₽')
        label_yuan.config(text=f'Юань\n¥--{get_exchange_rate("R01375")}₽')

date = datetime.datetime.today().strftime('%d/%m/%Y')
url_main = f'http://www.cbr.ru/scripts/XML_daily.asp?date_req={date}'
params = {'date_req': date}


window = Tk()
window.geometry('900x1000+800+300')
window["bg"] = '#0000FF'
window.resizable(width=False, height=False)
window.title('Валюты')

label = Label(text='Курс валют.\nПеревод денег в рубли', bg='yellow', fg='#0000FF', font=('Arial', 45))
label.place(x=130, y=40, width=650)

label_usd = Label(text=f'Доллары\n$--{get_exchange_rate("R01235")}₽', bg='yellow', fg='#0000FF', font=('Arial', 35))
label_usd.place(x=100, y=300, width=340)

label_eur = Label(text=f'Евро\n€--{get_exchange_rate("R01239")}₽', bg='yellow', fg='#0000FF', font=('Arial', 35))
label_eur.place(x=100, y=450, width=340)

label_yuan = Label(text=f'Юань\n¥--{get_exchange_rate("R01375")}₽', bg='yellow', fg='#0000FF', font=('Arial', 35))
label_yuan.place(x=100, y=600, width=340)

img = PhotoImage(file='flag.png')
img_label = Label(image=img, bg= '#0000FF')
img_label.place(x=630, y=280)

button = Button(text='Дальше =>', font=('Arial', 25), bg='#00FF00', fg='#0000FF', command=next)
button.place(x=600, y=420)

window.mainloop()