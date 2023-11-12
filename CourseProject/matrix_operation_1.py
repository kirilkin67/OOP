# Импортируем из модуля math
import math


# Функция для умножения матриц
def matrix_multiplication(matrix1, matrix2):
    # Вычисляем размерность матрицы
    n = len(matrix1[0])
    m = len(matrix1)
    p = len(matrix2[0])
    q = len(matrix2)


    # Проверяем корректность матриц
    if (n != p) or (m != q):
        raise ValueError("Матрицы несовместимы")


    # Вычисляем размерность результата
    r = n * m
    s = p * q


    # Инициализируем пустую матрицу
    result = [[0 for j in range(s)] for i in range(r)]


    # Выполняем умножение матриц
    for i in range(r):
        for j in range(p):
            for k in range(q):
                result[i][j] += matrix1[i][k] * matrix2[k][j]


    # Возвращаем полученную матрицу
    return result


    # Функция для сложения матриц
def matrix_addition(matrix1, matrix2):
    # Вычисляем размерность матрицы
    n = len(matrix1[0])
    m = len(matrix1)
    p = len(matrix2[0])
    q = len(matrix2)


    # Проверяем корректность матриц
    if (n != p) or (m != q):
        raise ValueError("Матрицы несовместимы")


    # Вычисляем размерность результата
    r = n * m
    s = p * q


    # Инициализируем пустую матрицу
    result = [[0 for j in range(s)] for i in range(r)]


    # Выполняем сложение матриц
    for i in range(r):
        for j in range(p):
            for k in range(q):
                result[i][j] += matrix1[i][k] + matrix2[k][j]


    # Возвращаем полученную матрицу
    return result


    # Функция для вычитания матриц
def matrix_subtraction(matrix1, matrix2):
    # Вычисляем размерность матрицы
    n = len(matrix1[0])
    m = len(matrix1)
    p = len(matrix2[0])
    q = len(matrix2)


    # Проверяем корректность матриц
    if (n != p) or (m != q):
        raise ValueError("Матрицы несовместимы")


    # Вычисляем размерность результата
    r = n * m
    s = p * q


    # Инициализируем пустую матрицу
    result = [[0 for j in range(s)] for i in range(r)]


    # Выполняем вычитание матриц
    for i in range(r):
        for j in range(p):
            for k in range(q):
                result[i][j] += matrix1[i][k] - matrix2[k][j]


    # Возвращаем полученную матрицу
    return result


    # Функция для деления матриц
def matrix_division(matrix1, matrix2):
    # Вычисляем размерность матрицы
    n = len(matrix1[0])
    m = len(matrix1)
    p = len(matrix2[0])
    q = len(matrix2)


    # Проверяем корректность матриц
    if (n != p) or (m != q):
        raise ValueError("Матрицы несовместимы")


    # Вычисляем размерность результата
    r = n * m
