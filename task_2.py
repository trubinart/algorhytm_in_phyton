"""
Задание 2.
Предложить еще какие-гибудь варианты (механизмы, библиотеки) оптимизации и
доказать (наглядно, кодом) их эффективность
"""
from recordclass import recordclass, make_dataclass
from collections import namedtuple
import sys
import numpy

"""
Можно для коллекций спользовать вместо NameTupple Recordclass и Dataobject. Recordclass и Dataobject 
весят меньше чем NameTupple и еще изменяемый объект.

В примере ниже NameTupple весит 64 байта, Recordclass - 48 байт, Dataobject - 40 байт.

"""
Point_1 = namedtuple('Point_1', ('x', 'y', 'z'))
ob_1 = Point_1(1, 2, 3)

print(ob_1)
print(sys.getsizeof(ob_1))

Point_2 = recordclass('Point_2', ('x', 'y', 'z'))
ob_2 = Point_2(1, 2, 3)

print(ob_2)
print(sys.getsizeof(ob_2))

ob_2.x = 10
ob_2.y = 20
ob_2.z = 30

print(ob_2)
print(sys.getsizeof(ob_2))


Point_3 = make_dataclass('Point_3', ('x', 'y', 'z'))
ob_3 = Point_3(1, 2, 3)

print(ob_3)
print(sys.getsizeof(ob_3))

ob_3.x = 10
ob_3.y = 20
ob_3.z = 30

print(ob_3)
print(sys.getsizeof(ob_3))


"""
Нашел еще использование Cython и CPython. Для многомерных массивов - Numpy. 
Но не смог с ними разобраться.

"""





