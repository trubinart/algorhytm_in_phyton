"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""
from collections import OrderedDict
from timeit import timeit

a = dict()
b = OrderedDict()

def dict_1():
    for key in range(1,100):
        a[key] = key
    return a

def ordered_dict_1():
    for key in range(1,100):
        b[key] = key
    return b

print(f'Добавление элементов')
print(f'dict_1 - {timeit("dict_1()",setup= "from __main__ import dict_1", number=100000)}')
print(f'ordered_dict_1 - {timeit("ordered_dict_1()",setup= "from __main__ import ordered_dict_1", number=100000)}')

def dict_2():
    for key in range(2,100):
        a.items()
    return a

def ordered_dict_2():
    for key in range(2, 100):
        b.items()
    return b

print(f'\nПолучение элементов')
print(f'dict_2 - {timeit("dict_2()",setup= "from __main__ import dict_2", number=100000)}')
print(f'ordered_dict_2 - {timeit("ordered_dict_2()",setup= "from __main__ import ordered_dict_2", number=100000)}')

def dict_3():
    for key in range(2,100):
        a.pop(key)
    return a

def ordered_dict_3():
    for key in range(2, 100):
        b.pop(key)
    return b

print(f'\nУдаление элементов')
print(f'dict_3 - {timeit("dict_3()",setup= "from __main__ import dict_3", number=1)}')
print(f'ordered_dict_3 - {timeit("ordered_dict_3()",setup= "from __main__ import ordered_dict_3", number=1)}')


'''
Во всех операция dict быстрее чем OrderedDict.
Как я понимаю, это связано с оптимизацией dict в последних версиях питона.
'''