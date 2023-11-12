# Импортируем из модуля math
import math


class Vector:
    """ Определяем класс Vector """

    def __init__(self, x: float = 0, y: float = 0, z: float = 0):
        self.x = x
        self.y = y
        self.z = z
        self.vector = (x, y, z)

    def __str__(self):
        return f"Координаты вектора - x: {self.x}, y: {self.y}, z: {self.z}"

    def __add__(self, other):
        """ Сложение двух векторов """
        result = [x + y for x, y in zip(self.vector, other.vector)]
        return Vector(result[0], result[1], result[2])

    def __sub__(self, other):
        """ Вычитание двух векторов """
        result = [x - y for x, y in zip(self.vector, other.vector)]
        return Vector(result[0], result[1], result[2])

    def __mul__(self, other):
        """ Скалярное произведение двух векторов """
        return sum([x * y for x, y in zip(self.vector, other.vector)])

    def len_vector(self):
        """ Вычисление длины вектора """
        return round(math.sqrt(sum([x ** 2 for x in self.vector])), 6)

    def normalize_vector(self):
        """ Нормализованный вектор, длина вектора равна 1 """
        length = self.len_vector()
        if length == 0:
            return self.vector
        return Vector(self.x / length, self.y / length, self.z / length)

    def add_vector(self, other):
        """ Сложение двух векторов """
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def sub_vector(self, other):
        """ Вычитание двух векторов """
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def mul_scalar_vector(self, scalar):
        """ Произведение вектора на число"""
        return Vector(self.x * scalar, self.y * scalar, self.z * scalar)

    def dot_product(self, other):
        """ Скалярное произведение двух векторов """
        return sum([x * y for x, y in zip(self.vector, other.vector)])

    def projection_vector_to_vector(self, other):
        """ Проекция вектора на другой вектор, возвращается длина проекции """
        if other.len_vector() == 0:
            raise ValueError("Вектор не может быть нулевым (0, 0, 0)")
        return self.dot_product(other) / other.len_vector()


if __name__ == "__main__":
    vector1 = Vector(3, 4, 3)
    print(vector1)
    normalize = vector1.normalize_vector()
    print(normalize)
    print(normalize.len_vector())
    print(vector1.mul_scalar_vector(3))
    vector2 = Vector(1, 1, 1)
    print(vector2)
    print(vector2.len_vector())
    print(vector1 * vector2)
    print(vector1.dot_product(vector2))
    print(vector1 + vector2)
    print(vector2.add_vector(vector1))
    print(vector2 - vector1)
    print(vector2.sub_vector(vector1))
    print(vector1.projection_vector_to_vector(vector2))

