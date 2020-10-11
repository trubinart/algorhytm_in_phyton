"""
Задание 3.
Определить количество различных подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените хеши и множества

арра:

рар
ра
ар
ара
р
а
"""
import hashlib

"""
Функция, которая выводит все подстроки во множество c использованием рекурсии.
"""
def take_substring_set(string, count = 0, set = set()):
    if count == len(string):
        for i in range(0, len(string)):
            set.add(string[i])
            set.add(string[:-i])
        set.remove('')
        return print(set)

    elif count < len(string):
        set.add(string[count:])
        take_substring_set(string, count +1, set)

"""
Функция, которая выводит хеши подстрок во множество и считает количество.
"""
def take_substring_hash(string, count = 0, set = set()):
    if count == len(string):
        for i in range(0, len(string)):
            set.add(hashlib.sha256(string[i].encode()).hexdigest())
            set.add(hashlib.sha256(string[:-i].encode()).hexdigest())
        set.remove(hashlib.sha256(''.encode()).hexdigest())
        return print(set, f'\nУникальных подстрок {len(set)}')

    elif count < len(string):
        set.add(hashlib.sha256(string[count:].encode()).hexdigest())
        take_substring_hash(string, count +1, set)


take_substring_set('123fg')
take_substring_hash('123fg')
