"""
Задание 2.**

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева)

Поработайте с доработанной структурой, позапускайте на реальных данных.
"""

class BinaryTree:
    def __init__(self, root_obj):
        self.root = root_obj
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if new_node < self.root or self.left_child == None:
            tree_obj = BinaryTree(new_node)
            tree_obj.left_child = self.left_child
            self.left_child = tree_obj
        else:
            print('Нельзя вставлять влево число БОЛЬШЕ корня')
            self.insert_right(new_node)

    def insert_right(self, new_node):
        if new_node > self.root or self.right_child == None:
            tree_obj = BinaryTree(new_node)
            tree_obj.right_child = self.right_child
            self.right_child = tree_obj
        else:
            print('Нельзя вставлять влево число МЕНЬШЕ корня')
            self.insert_left(new_node)

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, obj):
        self.root = obj

    def get_root_val(self):
        return self.root


r = BinaryTree(8)
print(r.get_root_val())

r.insert_left(4)
r.insert_left(10)
print(r.get_left_child().get_root_val())
print(r.get_right_child().get_root_val())


r.insert_right(12)
r.insert_right(1)
print(r.get_right_child())
print(r.get_left_child())
print(r.get_left_child().get_root_val())
print(r.get_right_child().get_root_val())
