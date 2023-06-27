class Matrix:

    def __init__(self, rows=None, columns=None, number=""):
        """
        Класс для создания матрицы
        :param rows: количество строк
        :param columns: количество колонок
        :param number: номер матрицы
        """
        self.matrix = False

        try:
            if rows and columns:
                self.rows = rows
                self.columns = columns
                self.matrix = [[0] * columns for _ in range(rows)]
            else:
                rows, columns = input(f"Введите размер(количество и размер строк) {number}матрицы, через пробел: > ") \
                    .split()
                self.rows = int(rows)
                self.columns = int(columns)
                self.matrix = self.init_matrix(number)
        except (ValueError, TypeError):
            print("Ожидается два значения")

    def init_matrix(self, number):
        """
        Ввод значений матрицы.
        :param number: Значения строки матрицы, через пробел
        :return: список значений строк матрицы
        """
        new_matrix = list()
        for n in range(self.rows):
            print(f"Введите {self.columns} значения {n + 1} строки {number}матрицы:")
            row = [float(num) if "." in num else int(num) for num in input("> ").split()]
            if len(row) != self.columns:
                return False
            new_matrix.append(row)
        return new_matrix

    def multiply_const_matrix(self, const):
        self.matrix = [[const * column for column in row] for row in self.matrix]
        return self

    def transposition_main_diagonal(self):
        matrix = list()
        for column in range(self.columns):
            matrix.append([])
            for row in range(self.rows):
                matrix[column].append(self.matrix[row][column])
        # matrix = [[self.matrix[m][n] for m in range(self.row)] for n in range(self.column)]
        return matrix

    def transposition_side_diagonal(self):
        row = self.rows - 1
        column = self.columns - 1
        matrix = [[self.matrix[row - m][column - n] for m in range(self.rows)] for n in range(self.columns)]
        return matrix

    def transposition_vertical_line(self):
        column = self.columns - 1
        matrix = [[self.matrix[n][column - m] for m in range(self.columns)] for n in range(self.rows)]
        return matrix

    def transposition_horizontal_line(self):
        row = self.rows - 1
        matrix = [[self.matrix[row - n][m] for m in range(self.columns)] for n in range(self.rows)]
        return matrix

    @staticmethod
    def get_minor_matrix(matrix, size, row, column):
        # new_matrix = [[0] * size for _ in range(size)]
        minor = Matrix(rows=size, columns=size)
        shift_row = 0
        for n in range(size):
            if n == row:
                shift_row = 1
            shift_column = 0
            for m in range(size):
                if m == column:
                    shift_column = 1
                minor.matrix[n][m] = matrix[n + shift_row][m + shift_column]
        return minor.matrix

    def calculate_determinant(self, matrix, size):
        """
        Нахождение детерминанта матрицы
        :param matrix: матрица(n x n)
        :param size: размер
        :return: значение детерминанта
        """
        det = 0
        sign = 1
        if size == 1:
            return matrix[0][0]
        elif size == 2:
            det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
            return det
        else:
            for column in range(size):
                minor = self.get_minor_matrix(matrix, size - 1, 0, column)
                det += (sign * matrix[0][column] * self.calculate_determinant(minor, size - 1))
                sign = -sign
            return det

    def cofactor_matrix(self):
        cofactor = Matrix(rows=self.rows, columns=self.rows)
        for row in range(self.rows):
            sign = 1 if (row % 2) == 0 else -1
            for column in range(self.columns):
                minor = self.get_minor_matrix(self.matrix, self.rows - 1, row, column)
                cofactor.matrix[row][column] = sign * self.calculate_determinant(minor, self.rows - 1)
                sign *= -1
        return cofactor.matrix

    def inverse_matrix(self, det):
        det = 1 / det
        inverse = Matrix(self.rows, self.rows)
        inverse.matrix = self.cofactor_matrix()
        inverse.matrix = inverse.transposition_main_diagonal()
        inverse.matrix = [[int(det * column * 100) / 100 for column in row] for row in inverse.matrix]
        return inverse

    @staticmethod
    def add_matrices(first, second):
        final = Matrix(first.rows, first.columns)
        for row in range(first.rows):
            for column in range(first.columns):
                final.matrix[row][column] = first.matrix[row][column] + second.matrix[row][column]
        return final

    @staticmethod
    def multiply_matrices(matrix_1, matrix_2):
        matrix = list()
        for k in range(matrix_1.rows):
            matrix.append([])
            for m in range(matrix_2.columns):
                c = 0
                for n in range(matrix_2.rows):
                    c += matrix_1.matrix[k][n] * matrix_2.matrix[n][m]
                matrix[k].append(c)
        return matrix

    def print_matrix(self):
        if self.matrix:
            print("Результирующая матрица:")
            for row in self.matrix:
                for elem in row:
                    print(f"{elem:>10.2f}", end=" ")
                print()
        else:
            print("Попробуйте ещё раз.")
