"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.
"""
from collections import deque
from timeit import timeit

a = [i for i in range(1,100)]
b = deque(a)

def list_1():
    for i in range(200, 300):
        a.append(i)
    return a

def deque_1():
    for i in range(200, 300):
        b.append(i)
    return a

print(f'Добавление элементов')
print(f'list_1 - {timeit("list_1()",setup= "from __main__ import list_1", number=10000)}')
print(f'deque_1 - {timeit("deque_1()",setup= "from __main__ import deque_1", number=10000)}')

def list_2():
    for i in range(200, 300):
        a.append(0)
    return a

def deque_2():
    for i in range(200, 300):
        b.append(0)
    return a

print(f'\nУдаление элементов')
print(f'list_2 - {timeit("list_2()",setup= "from __main__ import list_2", number=10000)}')
print(f'deque_2 - {timeit("deque_2()",setup= "from __main__ import deque_2", number=10000)}')

def list_3():
    for i in range(1, 200):
        c = a[i]
    return c

def deque_3():
    for i in range(1, 200):
        c = b[i]
    return c

print(list_3())

print(f'\nПолучение элементов')
print(f'list_3 - {timeit("list_3()",setup= "from __main__ import list_3", number=100000)}')
print(f'deque_3 - {timeit("deque_3()",setup= "from __main__ import deque_3", number=100000)}')

'''
В результате проведенных замеров мы видим, что:
1. Добавление элементов быстрее работает в deque. Но только на больших количествах итераций. 
   Если делать добавление на 10-100 операциях, то разница во времени будет не значительной.
2. Удаление элементов быстрее происходит в list.
3. Получение элементов так же быстрее происходит в list на 10 000 итераций, 
   но на 100 000 итераций - в deque.
   
На большом количестве итераций документация права. На малом - нет.
'''