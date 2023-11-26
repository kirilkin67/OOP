# Импортируем из модуля math
import math


# Определяем класс Stack
class Stack:
    def __init__(self):
        self.items = []


    # Добавляем элемент в стек
    def push(self, item):
        self.items.append(item)


    # Извлекаем элемент из стека
    def pop(self):
        if len(self.items) == 0:
            raise EmptyStackError("Стек пуст")
        else:
            return self.items.pop()


    # Возвращаем длину стека
    def size(self):
        return len(self.items)


    # Проверяем, пуст ли стек
    def is_empty(self):
        return len(self.items) == 0


    # Возвращаем элемент из стека по индексу
    def item(self, index):
        if index >= len(self.items):
            raise IndexError("Элемент не найден")
        else:
            return self.items[index]


    # Возвращаем список элементов стека
    def list(self):
        return self.items


    # Реализуем оператор == для класса Stack
    def __eq__(self, other):
        if isinstance(other, Stack):
            return len(self.items) == len(other.items) and all(self.item(i) == other.item(i) for i in range(len(self.items)))
        else:
            return False


    # Реализуем оператор != для класса Stack
    def __ne__(self, other):
        return not self.__eq__(other)


    # Реализуем оператор < для класса Stack
    def __lt__(self, other):
        if isinstance(other, Stack):
            return len(self.items) < len(other.items)
        else:
            return False


    # Реализуем оператор <= для класса Stack
    def __le__(self, other):
        if isinstance(other, Stack):
            return len(self.items) <= len(other.items)
        else:
            return False


    # Реализуем оператор > для класса Stack
    def __gt__(self, other):
        if isinstance(other, Stack):
            return len(self.items) > len(other.items)
        else:
            return False


    # Реализуем оператор >= для класса Stack
    def __ge__(self, other):
        if isinstance(other, Stack):
            return len(self.items) >= len(other.items)
        else:
            return False


    # Реализуем оператор + для класса Stack
    def __add__(self, other):
        if isinstance(other, Stack):
            return Stack(self.items + other.items)
        else:
            raise TypeError("Стек не может быть сложен со значением типа {}".format(type(other)))


    # Реализуем оператор - для класса Stack
    def __sub__(self, other):
        if isinstance(other, Stack):
            return Stack(self.items - other.items)
        else:
            raise TypeError("Стек не может быть вычтен со значением типа {}".format(type(other)))


    # Реализуем оператор * для класса Stack
    def __mul__(self, other):
        if isinstance(other, Stack):
            return Stack(self.items * other.items)
        else:
            raise TypeError("Стек не может быть возведен в степень типа {}".format(type(other)))