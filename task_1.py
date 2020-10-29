"""
Задание 1.
Реализуйте кодирование строки "по Хаффману".
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на пример с урока, сделать свою версию алгоритма
Разрешается и приветствуется изменение имен переменных, выбор других коллекций, различные изменения
и оптимизации.
КОПИПАСТ ПРИМЕРА ПРИНИМАТЬСЯ НЕ БУДЕТ!
2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например, через ООП или предложить иной подход к решению.

ВНИМАНИЕ: примеры заданий будут размещены в последний день сдачи.
Но постарайтесь обойтись без них.
"""

from collections import Counter, deque

text = 'beep boop beer!'
frequency = Counter(text)
frequency_list = deque(sorted(frequency.items(), key=lambda x: x[1]))

while len(frequency_list) > 1:
    weight = frequency_list[0][1] + frequency_list[1][1]
    summary = {0: frequency_list.popleft()[0],
               1: frequency_list.popleft()[0]}

    if len(frequency_list) == 0:
        frequency_list.append((summary, weight))
        break

    for i, value in enumerate(frequency_list):
        if weight > value[1]:
            continue
        else:
            frequency_list.insert(i, (summary, weight))
            break

    else:
        frequency_list.append((summary, weight))
frequency_list = frequency_list[0][0]
print(frequency_list)

table_code = dict()

def haffman_code(tree, path=''):
    # Если элемент не словарь, значит мы достигли самого символа
    # и заносим его, а так же его код в словарь (кодовую таблицу).
    if not isinstance(tree, dict):
        table_code[tree] = path
    # Если элемент словарь, рекурсивно спускаемся вниз
    # по первому и второму значению (левая и правая ветви).
    else:
        haffman_code(tree[0], path=f'{path}0')
        haffman_code(tree[1], path=f'{path}1')

haffman_code(frequency_list)
print(table_code)

for i in table_code:
    print(table_code[i], end=' ')

