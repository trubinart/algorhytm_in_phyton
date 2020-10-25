"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, ...

arr[m]
from statistics import median
"""
from statistics import median
import random
import copy


m = int(input('Введите m: '))
orig_list = [random.randint(-100, 100) for _ in range((2*5)+1)]
print(orig_list)

i = 0
for num in orig_list:
    for num_2 in orig_list:
        if num > num_2:
            result = num
            i += 1
    if i == len(orig_list) // 2:
        result = num
        break
    i = 0

print(f'Медиана моего кода {result} \n')

orig_list.sort()
print(orig_list)
print(f'Медиана модуля MEDIAN {median(orig_list)}')

