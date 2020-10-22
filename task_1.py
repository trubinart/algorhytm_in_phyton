"""
Задание 1.
Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Можно взять задачи с курса Основ или с текущего курса Алгоритмов

Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""
from memory_profiler import profile

#ПРОГРАММА 1
@profile
def sum_list(list:str) -> int:
    finish_sum = 0
    for i in range(0, len(user_ask)):
        num = int(user_ask[i])
        finish_sum += num
    return finish_sum


user_ask = input('Введите числа через пробел:')
result = 0
while True:
    if user_ask != 'end':
        user_ask = user_ask.split()
        middle_result = sum_list(user_ask)
        result = result + middle_result
        print(f'Сумма ваших чисел {result}')
        user_ask = input('Введите еще числа (оставноить программу "end"):')
    else:
        print(f'Программа завершена, ваша сумма {result}')
        break


#ПРОГРАММА 2
from functools import reduce

def multiply(previous_num, next_num):
    return previous_num * next_num

@profile
def factotorial(num):
    list_factorial = []
    i = 1
    while i <= num:
        for i in range(i, num + 1):
            list_factorial.append(i)
            factorial_value = reduce(multiply, list_factorial)
            i +=1
            return factorial_value

for i in factotorial(7):
    print(i)

#ПРОГРАММА 3
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

@profile
def func_4():
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

func_4()


'''
Выводы:
Взял три программы: две из основ питона и одну с вашего курса. Не смог найти программу, где бы шло заполнение
большой по объему коллекции. 

Из приведенных ниже отчетов профилирования видно, что все программы не являются ресурсопортебялемыми с точки зрения 
памяти. У меня стоит Python 3.8, процессор 64 разряда.

В моей версии профилировщика появился новый столбец, которого не было на уроке - Occupences. Как я понял, это отображение
количество действий, которые выполняет программа на каком-то шаге.

Если опираться на столбец Occupences, то самая нересурсоемкая программа - #2, так как все строки выполняеются
по одному разу.


ПРОГРАММА 1
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    19     13.2 MiB     13.2 MiB           1   @profile
    20                                         def sum_list(list:str) -> int:
    21     13.2 MiB      0.0 MiB           1       finish_sum = 0
    22     13.2 MiB      0.0 MiB          11       for i in range(0, len(user_ask)):
    23     13.2 MiB      0.0 MiB          10           num = int(user_ask[i])
    24     13.2 MiB      0.0 MiB          10           finish_sum += num
    25     13.2 MiB      0.0 MiB           1       return finish_sum

ПРОГРАММА 2
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    48     13.1 MiB     13.1 MiB           1   @profile
    49                                         def factotorial(num):
    50     13.1 MiB      0.0 MiB           1       list_factorial = []
    51     13.1 MiB      0.0 MiB           1       i = 1
    52     13.1 MiB      0.0 MiB           1       while i <= num:
    53     13.1 MiB      0.0 MiB           1           for i in range(i, num + 1):
    54     13.1 MiB      0.0 MiB           1               list_factorial.append(i)
    55     13.1 MiB      0.0 MiB           1               factorial_value = reduce(multiply, list_factorial)
    56     13.1 MiB      0.0 MiB           1               i +=1
    57     13.1 MiB      0.0 MiB           1               return factorial_value

ПРОГРАММА 3
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    80     13.1 MiB     13.1 MiB           1   @profile
    81                                         def func_4():
    82                                             while True:
    83     13.2 MiB      0.0 MiB           2           ask_number_1 = input('Введите первое число в 16-ой системе (q - выход) : ')
    84                                         
    85     13.2 MiB      0.0 MiB           2           if ask_number_1 == 'q':
    86     13.2 MiB      0.0 MiB           1               print('Скрипт завершен')
    87     13.2 MiB      0.0 MiB           1               break
    88                                         
    89     13.2 MiB      0.0 MiB           1           ask_number_2 = input('Введите второе число в 16-ой системе q - выход) : ')
    90                                         
    91     13.2 MiB      0.0 MiB           1           if ask_number_2 == 'q':
    92                                                     print('Скрипт завершен')
    93                                                     break
    94                                         
    95                                                 else:
    96     13.2 MiB      0.0 MiB           1               try:
    97     13.2 MiB      0.0 MiB           1                   ask_1 = int(ask_number_1, 16)
    98     13.2 MiB      0.0 MiB           1                   ask_2 = int(ask_number_2, 16)
    99                                         
   100                                                     except ValueError:
   101                                                         print('Одно из чисел не является шестнадцаричным, попробуйте снова!')
   102                                                         continue
   103                                         
   104     13.2 MiB      0.0 MiB           1               a = Number(ask_number_1)
   105     13.2 MiB      0.0 MiB           1               b = Number(ask_number_2)
   106     13.2 MiB      0.0 MiB           1               c = a + b
   107     13.2 MiB      0.0 MiB           1               d = a * b
   108                                         
   109     13.2 MiB      0.0 MiB           1               print(f'Сумма чисел {c.list}')
   110     13.2 MiB      0.0 MiB           1               print(f'Произведение числе {d.list}')

'''