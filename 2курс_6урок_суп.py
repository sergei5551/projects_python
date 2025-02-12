import requests
from bs4 import BeautifulSoup
import datetime

date = datetime.datetime.today().strftime('%d/%m/%Y')

url_main = 'https://cbr.ru/scripts/XML_daily.asp'
url_date = f'?date_req={date}'

valuts_id = ['R01235', 'R01239', 'R01335', 'R01355', 'R01135']


def get_exchange_rate(valute_from, amount, valute_to):
    response = requests.get(url_main + url_date)
    soup = BeautifulSoup(response.content, 'xml')
    znach = soup.find_all('Valute')
    # Поиск строчек с нашими валютами
    for i in znach:
        if i.CharCode.text == valute_from:
            w_from = i
            str_val_in_float_from = str((w_from.Value.text)[:2]) + '.' + str((w_from.Value.text)[3:])
        elif i.CharCode.text == 'RUR':
            pass
        elif i.CharCode.text == valute_to and i.CharCode.text != 'RUR':
            w_to = i
            str_val_in_float_to = str((w_to.Value.text)[:2]) + '.' + str((w_to.Value.text)[3:])

    # Я использовал законы математики(пропорции), чтоб узнать на сколько одна валюта отличается от другой.
    # Когда получаемая валюта равна рублям
    if valute_to == 'RUR':
        if (int(w_from.Nominal.text) * amount) == amount:
            print(
                f'{amount} {w_from.find("Name").text} стоит {amount * str_val_in_float_from} рублей',end='\n')
        else:
            print(
                f'{amount} {w_from.find("Name").text} стоит {float(str_val_in_float_from) / amount} рублей', end='\n')

    # Когда получаемая валюта не равна рублям
    else:
        if (int(w_from.Nominal.text) * amount) == amount:
            print(
                f'{amount} {w_from.find("Name").text} стоит {amount * float(str_val_in_float_to) / float(str_val_in_float_from)} {w_to.find("Name").text}',
                end='\n')
        else:
            print(
                f'{amount} {w_from.find("Name").text} стоит {amount * float(str_val_in_float_to)/ (float(str_val_in_float_from) / amount) } {w_to.find("Name").text}',
                end='\n')


valute_from = "EUR"  # Валюта изначальная
valute_to = "RUR"  # Валюта в которую будем конвертировать
amount = 1  # int(input('Введите количество конвертируемой валюты'))
get_exchange_rate(valute_from, amount, valute_to)
