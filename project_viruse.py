from tkinter import *

def close():
    global counter
    if counter>0:
        counter -= 1
        label_2['text'] = counter
        label_2.place(x=10, y=200, width=650, height=100)
        window.after(1000,close)
    else:
        width = str(window.winfo_screenwidth())
        height = str(window.winfo_screenheight())
        window.geometry(width+'x'+height)

        photo = PhotoImage(file='RdsN.gif')
        label_photo = Label(image=photo)
        label_photo.image = photo
        label_photo.place(x=100 , y=100)
counter = 60

window = Tk()
window.title('Троян')
window.geometry('700x500')
window.resizable(width=False, height=False)
window.config(bg='black')

label = Label(text='На вашем компьютере вирус!', font=('Courier New', 20), bg='black', fg='red')
label.place(x=10, y=30, width=650, height=100)

label_2= Label(text=counter, font=('Courier New', 20), bg='black', fg='red')


button = Button(text='Закрыть', font=('TimesNewRoman', 30))
button.place(x=250,y=400)

window.protocol("WM_DELETE_WINDOW", close)

window.mainloop()