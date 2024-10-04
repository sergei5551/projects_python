from tkinter import *
from random import randint

photos = {1: "1.png",
          2: "2.jpg",
          3: "3.png",
          4: "4.png",
          5: "5.png"
}

random_names = {1: 'Леон',
                2: 'Мортис',
                3: 'Беа',
                4: 'Роза',
                5: 'Эль примо'
                }
# Программа ввода данных для дальнейшего использования
def Copy():
    flag=False
    if len(entry1.get()) == 16 and  len(entry2.get()) == 3 and len(entry3.get()) == 7:
        label_number ['text']= f'Данные: \n{entry1.get()}\n{entry2.get()}\n{entry3.get()} '
        random_name()
    else:
        label_number['text'] = 'Попробуйте еще раз'

def random_name():
    random_numbers=randint(1, 5)
    window_2 = Tk()
    window_2.geometry('400x400')


    lebel = Label(window_2, text=random_names[random_numbers] , font=("Courier", 20))
    lebel.pack()

    canvas = Canvas(window_2, width=500, height=500)
    canvas.pack()

    photo_obj = PhotoImage(file=photos[random_numbers])
    canvas.create_image(50, 50, image=photo_obj)
    '''file = photos[random_numbers]'''
    window_2.mainloop()

window = Tk()
window.title('Тест на бравл старс')
window.geometry('500x600')
window.resizable(width=False, height=False)

# Текст
label = Label(text='Кто ты из бравл старса?',
              font=("Courier", 20),
              height = 2,
              )
label.pack()

label2 = Label(text='Введите данные карты и \nузнайте кто вы из \nбравл старс!',
              font=("Courier", 20)
              )
label2.place(x= 70, y=215)

label_number = Label(text='Введите \nточные данные карты',
                     font=("Courier", 20))
label_number.place(x=100,y=400)


# Панели ввода
entry1 = Entry(window,
              bg='red',
              width=21,
              font=("Courier", 20)
              )
entry1.insert(0, 'Номер карты:')
entry1.place(x=81, y=310)

entry2 = Entry(window,
              bg='red',
              width=8,
              font=("Courier", 20)
              )
entry2.insert(0, 'CVC2/CVV2')
entry2.place(x=81, y=350)

entry3 = Entry(window,
              bg='red',
              width=10,
              font=("Courier", 20)
              )
entry3.insert(0, '00/0000')
entry3.place(x=257, y=350)

# Кнопка
button = Button(
    text='Отправить',
    width=20,
    height=4,
    bg='red',
    fg='white',
    font=('TamesNeuRoman', 20),
    command=Copy)
button.pack()


window.mainloop()