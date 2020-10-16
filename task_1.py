"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""
import timeit

def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

def func_2(nums):
    new_arr = []
    for i in nums:
        if i % 2 == 0:
            new_arr.append(nums.index(i))
    return new_arr

nums = [1, 2, 3, 4, 5]
print('func_1', timeit.timeit('func_1(nums)', setup= 'from __main__ import func_1, nums'))
print('func_2', timeit.timeit('func_2(nums)', setup= 'from __main__ import func_2, nums'))

"""
ВЫВОД:
Удалось снизить время выполенения кода за счет того, что я не считаю длинну списка, 
а сразу беру элемент из списка, проверяю его и беру индекс, если он четный.

Получилось уменьшить выполнение алгоритма на одну операцию - высчитывание
длинны списка.
"""