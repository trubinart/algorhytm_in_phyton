"""
Задание 7.
Задание на закрепление навыков работы с очередью

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "доска задач".


Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения

После реализации структуры, проверьте ее работу на различных сценариях
"""
class TaskBoard:
    def __init__(self):
        self.list_for_solving = []
        self.list_for_correction = []

    def show_list_for_solving(self):
        print(self.list_for_solving)

    def show_list_for_correction(self):
        print(self.list_for_correction)

    def add_list_for_solving(self, el):
        self.list_for_solving.append(el)

    def take_task (self):
        print(self.list_for_solving[-1])
        self.list_for_solving.pop(-1)

    def correct_task (self):
        print(self.list_for_solving[-1])
        self.list_for_correction.append(self.list_for_solving[-1])
        self.list_for_solving.pop(-1)

    def finish_correct_task (self):
        self.list_for_correction.pop(-1)

    def is_empty_solving(self):
        self.list_for_solving == []

    def is_empty_correction(self):
        self.list_for_correction == []

if __name__ == '__main__':
    a = TaskBoard()
    a.add_list_for_solving('task1')
    a.add_list_for_solving('task2')
    a.add_list_for_solving('task3')
    a.add_list_for_solving('task4')
    a.show_list_for_solving()
    a.take_task()
    a.show_list_for_solving()
    a.show_list_for_correction()
    a.correct_task()
    a.show_list_for_correction()
    a.show_list_for_solving()
    a.finish_correct_task()
    a.show_list_for_correction()


