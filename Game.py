import tkinter
import random
window = tkinter.Tk()
w = 680
h = 600

window.geometry(f'{w}x{h}+770+180')
window.title('окно')

canvas = tkinter.Canvas(window, width=w, height=h)
bg_image = tkinter.PhotoImage(file='D:/4/zamok.png')
canvas.pack()

# Шаблоны
class Knight:
    def __init__(self):
        self.x = 90
        self.y = h // 2

        self.dy = 0
        self.dx = 0

        self.image = tkinter.PhotoImage(file='D:/4/16.png')
    def up(self, event):
        self.dy = -3
    def down(self, event):
        self.dy = +3
    def left(self, event):
        self.dx = -3
    def right(self, event):
        self.dx = +3
    def stop(self, event):
        self.dy = 0
        self.dx = 0
class Dragon:
    def __init__(self):
        self.x = w-50
        self.y = random.randint(50, h-50)

        self.dy = random.randint(1, 3)
        self.dx = random.randint(2, 4)

        self.image = tkinter.PhotoImage(file='D:/4/dragon.png')

# Создание персонажей
hero = Knight()
dragons = []
for i in range(3):
    dragons.append(Dragon())


def game():
    canvas.delete('all')
    canvas.create_image(w // 2, h // 2, image=bg_image)
    canvas.create_image(hero.x, hero.y, image=hero.image)
    if 70 <= hero.y <= h - 70:
        hero.y = hero.y + hero.dy
    elif hero.y > h - 70:
        hero.y -= 1
    elif hero.y < 70:
        hero.y += 1
    hero.x = hero.x + hero.dx


    current_dragon = 0
    dragon_to_kill = -1

    for dragon in dragons:
        canvas.create_image(dragon.x, dragon.y, image=dragon.image)
        dragon.x = dragon.x - dragon.dx
        if (dragon.x - hero.x) ** 2 + (dragon.y - hero.y) ** 2 <= (75+75) ** 2 + (75+75) ** 2:
            dragon_to_kill = current_dragon

        if dragon.x < 0:
            canvas.delete('all')
            canvas.create_text(w // 2, h // 2, text='Проигрыш, Олух', font=('Arial', 40))
            return

        current_dragon += 1

    if dragon_to_kill != -1:
        del dragons[dragon_to_kill]

    if dragons == []:
        canvas.delete('all')
        canvas.create_text(w//2, h//2, text='Ты победил, красавчик', font=('Arial', 40))
        return

    window.after(5, game)
game()

# Управление

window.bind('<Key-Up>', hero.up)
window.bind('<Key-Down>', hero.down)
window.bind('<Key-Left>', hero.left)
window.bind('<Key-Right>', hero.right)
window.bind('<KeyRelease>', hero.stop)

window.mainloop()
