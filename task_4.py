"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""
import timeit

array = [1, 3, 1, 3, 4, 5, 1]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3(array, result = 0):
    memory = set()
    for i in array:
        if i in memory:
            continue
        if array.count(i) > result:
            result = array.count(i)
            number = i
            memory.add(i)
    return f'Число {number} встречается {result} раз(а)'

def func_4(array, result = 0):
    for i in array:
        if array.count(i) > result:
            result = array.count(i)
            number = i
        return f'Число {number} встречается {result} раз(а)'



print(func_1())
print(func_2())
print(func_3(array))
print(func_4(array))

print(f'func_1 {timeit.timeit("func_1()", setup="from __main__ import func_1, array", number=1000)}')
print(f'func_2 {timeit.timeit("func_2()", setup="from __main__ import func_2, array", number=1000)}')
print(f'func_3 {timeit.timeit("func_3(array)", setup="from __main__ import func_3, array", number=1000)}')
print(f'func_4 {timeit.timeit("func_4(array)", setup="from __main__ import func_4, array", number=1000)}')

"""
Сделал вариант с мепоризацией, он работате лучше чем вторая функция, но не самый быстрый.
В итоге реализовал просто алгоритм из трех действий вместо 6 в первом алгоритме. Получилось ускорить.
"""