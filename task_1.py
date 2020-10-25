"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""
import random
import timeit
import copy

orig_list = [random.randint(-100, 100) for _ in range(10)]
print(orig_list)
orig_list_2 = copy.deepcopy(orig_list)
orig_list_3 = copy.deepcopy(orig_list)


#ВАРИАНТ БЕЗ ОПТИМИЗАЦИИ
def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            a = lst_obj[i+1]
            b = lst_obj[i]
            if lst_obj[i+1] > lst_obj[i]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj

bubble_sort(orig_list_2)
print(orig_list_2)

#ВАРИАНТ С ОПТИМИЗАЦИЕЙ
def bubble_sort_2(lst_obj):
    n = 1
    while n < len(lst_obj):
        list_copy = copy.deepcopy(lst_obj)
        for i in range(len(lst_obj)-n):
            a = lst_obj[i+1]
            b = lst_obj[i]
            if lst_obj[i+1] > lst_obj[i]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        if list_copy == lst_obj:
            break
        n += 1
    return lst_obj

bubble_sort_2(orig_list_3)
print(orig_list_2)

#ЗАМЕРЫ
print(timeit.timeit("bubble_sort(orig_list_2)", \
    setup="from __main__ import bubble_sort, orig_list_2", number=100000))

print(timeit.timeit("bubble_sort(orig_list_3)", \
    setup="from __main__ import bubble_sort, orig_list_3", number=100000))

"""
Вывод:
Оптимизация дала результат улучшения. 
Без оптимизации время выполнения на 100 000 итераций составила 1.15161377 сек, с оптимизацией - 1.134538029 сек.
Это произошло за счет того, что мы не провоходим список циклом в пустую. Значит уменьшили количество операций
для достижения результата.

"""