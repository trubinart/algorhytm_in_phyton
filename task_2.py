"""
2.	Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)
"""

from collections import deque

class Number:
    def __init__(self, num):
        self.num = num
        _result_list = list(num)
        del _result_list[0:2]
        self.list = deque(map(str.upper, _result_list))

    def __add__(self, other):
        result = int(self.num, 16) + int(other.num, 16)
        return Number(hex(result))

    def __mul__(self, other):
        result = int(self.num, 16) * int(other.num, 16)
        return Number(hex(result))

while True:
    ask_number_1 = input('Введите первое число в 16-ой системе (q - выход) : ')

    if ask_number_1 == 'q':
        print('Скрипт завершен')
        break

    ask_number_2 = input('Введите второе число в 16-ой системе q - выход) : ')

    if ask_number_2 == 'q':
        print('Скрипт завершен')
        break

    else:
        try:
            ask_1 = int(ask_number_1, 16)
            ask_2 = int(ask_number_2, 16)

        except ValueError:
            print('Одно из чисел не является шестнадцаричным, попробуйте снова!')
            continue

        a = Number(ask_number_1)
        b = Number(ask_number_2)
        c = a + b
        d = a * b

        print(f'Сумма чисел {c.list}')
        print(f'Произведение числе {d.list}')
