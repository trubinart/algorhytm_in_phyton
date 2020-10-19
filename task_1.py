"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Рога
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога

Предприятия, с прибылью ниже среднего значения: Копыта
"""
from collections import namedtuple, defaultdict

quater = namedtuple('Quater', 'q1 q2 q3 q4 average')
dict_in_common = defaultdict(int)

ask_number = int(input('Введите количество предприятий для расчета прибыли: '))

i = 0
while i < ask_number:
    ask_name = input('Введите название предприятия: ')
    ask_q = input('Через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): ').split()
    dict_in_common[ask_name] = list(map(int, ask_q))
    dict_in_common[ask_name].append(sum(dict_in_common[ask_name]) / len(dict_in_common[ask_name]))
    i+=1

print(f'\n{dict_in_common}')

avarage_profit = []
for key, value in dict_in_common.items():
    avarage_profit.append(value[4])

avarage_profit = sum(avarage_profit)/len(avarage_profit)
print(f'\n{avarage_profit}')

low_company = defaultdict(int)
high_company = defaultdict(int)

for key, value in dict_in_common.items():
    if value[4] < avarage_profit:
        low_company[key] = value[4]
    else:
        high_company[key] = value[4]

print(f'\nКомпании, у которых прибыль НИЖЕ средней: ')
for key, value in low_company.items():
    print(f'Копания - {key} со средней прибылью - {value}')

print(f'\nКомпании, у которых прибыль ВЫШЕ средней: ')
for key, value in high_company.items():
    print(f'Копания - {key} со средней прибылью - {value}')
