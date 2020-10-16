"""
Задание 3.

Приведен код, формирующий из введенного числа
2обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""
import cProfile, timeit

def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num

cProfile.run('revers(213123245434345465676879667563455)')
cProfile.run('revers_2(213123245434345465676879667563455)')
cProfile.run('revers_3(213123245434345465676879667563455)')

enter_num = 213123245434345465676879667563455
print(f'revers {timeit.timeit("revers(enter_num)", setup="from __main__ import revers, enter_num", number=1000)}')
print(f'revers_2 {timeit.timeit("revers_2(enter_num)", setup="from __main__ import revers_2, enter_num", number=1000)}')
print(f'revers_3 {timeit.timeit("revers_3(enter_num)", setup="from __main__ import revers_3, enter_num", number=1000)}')

print(revers_3(enter_num))

"""
Третья реализация самая быстрая, так как не используетя промежучтоную переменную для храния
и выполнятся только в три дейстия. Так же на скорость влияет взяитие среза - 
то стандартная операция, кототрая оптимизирована под быстройдействие.

Вторая реализация хоть быстрее первый за счет отсутствия рекурсии, но медленнее третье, так
как идет применение промежуточной переменной и алгоритм выполняет 4 действия вместо трех.

Первая реализация самая медленная, так как в ней используется рекурсия.
"""