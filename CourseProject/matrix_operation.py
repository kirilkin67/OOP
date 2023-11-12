class Matrix:

    def __init__(self, rows: int = 0, columns: int = 0):
        """
        Класс для создания матрицы
        :param rows: количество строк
        :param columns: количество колонок
        """
        self.rows = rows
        self.columns = columns
        self.matrix = [[0] * columns for _ in range(rows)]

    def __str__(self):
        result_matrix = ''
        for row in self.matrix:
            result_row = ''
            for elem in row:
                result_row += f'{elem:>10.2f}'
            result_matrix += f'\n{result_row}'
        return f'Результирующая матрица:{result_matrix}'

    def __getitem__(self, indices):
        row, col = indices
        return self.matrix[row][col]

    def __setitem__(self, indices, value):
        row, col = indices
        self.matrix[row][col] = value

    def __add__(self, other):
        """ Сложение матриц"""
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Матрицы должны иметь одинаковые размеры")
        result = Matrix(self.rows, self.columns)
        for row in range(self.rows):
            for column in range(self.columns):
                result.matrix[row][column] = self.matrix[row][column] + other.matrix[row][column]
        return result

    def __sub__(self, other):
        """ Вычитание матриц"""
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Матрицы должны иметь одинаковые размеры")
        result = Matrix(self.rows, self.columns)
        for row in range(self.rows):
            for column in range(self.columns):
                result.matrix[row][column] = self.matrix[row][column] - other.matrix[row][column]
        return result

    def __mul__(self, scalar):
        """ Умножение матрицы на число"""
        result = Matrix(self.rows, self.columns)
        result.matrix = [[scalar * column for column in row] for row in self.matrix]
        return result

    def init_row(self, index, value: list):
        """
        Ввод значений матрицы.
        :param index: Значения строки матрицы
        :param value: список значений строки матрицы
        """
        row = index
        if len(value) == self.columns:
            self.matrix[row] = value
        else:
            raise ValueError("Количество значений должно быть равно количеству колонок")

    def init_matrix(self, value: list):
        """
        Инициализация матрицы из списка значений list(list()).
        Количество значений списков должно быть одинаковым
        :param: Список значений строк матрицы
        """
        self.rows = len(value)
        self.columns = len(value[0])
        for row in value:
            if len(row) != self.columns:
                raise ValueError("Количество значений должно быть одинаковым")
        self.matrix = value

    def multiply(self, other):
        """
        Умножение двух матриц.
        Количество столбцов в первой матрице должно быть равно количеству строк во второй матрице
        """
        if self.columns != other.rows:
            raise ValueError(
                "Количество столбцов в первой матрице должно быть равно количеству строк во второй матрице")
        result = Matrix(self.rows, other.columns)
        for row in range(self.rows):
            for column in range(other.columns):
                for k in range(self.columns):
                    result[row, column] += self[row, k] * other[k, column]
        return result

    def transposition_main_diagonal(self):
        """ Транспонирование матрицы """
        result = Matrix(self.columns, self.rows)
        for column in range(self.columns):
            for row in range(self.rows):
                result[column, row] = self.matrix[row][column]
        return result


if __name__ == "__main__":
    m0 = Matrix(1, 2)
    m0[0, 0] = 10
    m0[0, 1] = 20

    m1 = Matrix(2, 3)
    m1.init_row(0, [1, 2, 3])
    m1.init_row(1, [4, 5, 6])

    m2 = Matrix()
    m2.init_matrix([[7, 8, 9], [10, 11, 12]])

    m3 = Matrix()
    m3.init_matrix([[1, 0, 1], [10, 11, 12], [20, 30, 12]])

    print(m0)
    print(m1)  # Output: 1 2 3 \n 4 5 6
    print(m2)  # Output: 7 8 9 \n 10 11 12
    print(m1 + m2)  # Output: 8 10 12 \n 14 16 18
    print(m1 - m2)  # Output: -6 -6 -6 \n -6 -6 -6
    print(m1 * 2)  # Output: 2 4 6 \n 8 10 12

    m_mul = m0.multiply(m2)
    print(m_mul)  # Output: 270 300 330
    print(m3)
    print(m3.transposition_main_diagonal())
    print(m2.transposition_main_diagonal())
