import random
def randoms():
    global znach
    g = random.randint(1, 2)
    znach = sl[g] # кто будет крушить лицо :3

class Units:

    def __init__(self, name_person):
        self.name = name_person
        self.health = 100
    def fighting(self):
        self.health = self.health - 20


unit_1 = Units('АРД')
unit_2 = Units('ЗВЕРПИЛЬ')
sl= {1: 'unit_1',
     2: 'unit_2'}

while (unit_1.health != 0) and (unit_2.health != 0):
    randoms()
    if znach == 'unit_1':
        print(f'Бьет {unit_1.name} противника {unit_2.name}!')
        unit_2.fighting()
        print(f'У противника, {unit_2.name}, осталось {unit_2.health}хп')
        с= input('продолжить...')
    elif znach == 'unit_2':
        print(f'Бьет {unit_2.name} противника {unit_1.name}!')
        unit_1.fighting()
        print(f'У противника, {unit_1.name}, осталось {unit_1.health}хп')
        с = input('продолжить...')


if unit_1.health == 0:
    print(f'Победил {unit_2.name}!')
elif unit_2.health == 0:
    print(f'Победил {unit_1.name}!')


