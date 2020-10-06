"""
Задание 6.
Задание на закрепление навыков работы со стеком

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим стеком порогового значения.
Реализуйте по аналогии с примером, рассмотренным на уроке, необходимые методы,
для реализации это структуры, добавьте новые методы (не рассмотренные в примере с урока)
для реализации этой задачи.

После реализации структуры, проверьте ее работу на различных сценариях
"""

class StackPlate():
    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []
        self.stack_3 = []

    def take_plate(self):
        if len(self.stack_1) != 0:
            self.stack_1.pop(-1)
        elif len(self.stack_2) != 0:
            self.stack_2.pop(-1)
        elif len(self.stack_3) != 0:
            self.stack_3.pop(-1)
        else:
            print ('Все стеки пусты')

    def add_plate(self, el):
        if len(self.stack_1) >= 5:
            self.stack_2.append(el)
        elif len(self.stack_2) >= 5:
            self.stack_3.append(el)
        elif len(self.stack_3) >= 5:
            print('Все стеки заполнены')
        else:
            self.stack_1.append(el)

    def show_steck(self):
        print(self.stack_1)
        print(self.stack_2)
        print(self.stack_3)

    def empty_steck(self):
        self.stack_1 = []
        self.stack_2 = []
        self.stack_3 = []

    def show_len(self):
        print(len(self.stack_1)+len(self.stack_2)+len(self.stack_3))

if __name__ == '__main__':
    a = StackPlate()
    a.take_plate()
    a.add_plate(1)
    a.add_plate(2)
    a.add_plate(3)
    a.show_steck()
    a.take_plate()
    a.show_steck()
    a.show_steck()
    a.show_len()