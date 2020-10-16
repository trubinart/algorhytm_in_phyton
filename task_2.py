"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Подсказка: примените мемоизацию

Добавьте аналитику: что вы сделали и почему
"""

from timeit import Timer

def memorize (func):
    def g(n, memory={}):
        r = memory.get(n)
        if not r:
            r = func(n)
            memory[n] = r
        return r
    return g

def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'

@memorize
def recursive_reverse2(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


number = 12345678912314144314143154365646757869
t1 = Timer('recursive_reverse(number)','from __main__ import recursive_reverse, number')
t2 = Timer('recursive_reverse2(number)','from __main__ import recursive_reverse2, number')

print(t1.timeit(number=1000))
print(t2.timeit(number=1000))

print(recursive_reverse(number))

""""
Применил дикоратор кеширования. За счет этого уменьшили нагрузку на оперативную память,
не создается хеш таблица в рамках рекурсии. Это и ускоряет выполнение программы.

'"""

