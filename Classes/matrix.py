MENU = """
1. Сложение 2 матриц
2. Умножение матрицы н число
3. Умножение матриц
4. Транспонирование матрицы
5. Детерминант матрицы
6. Inverse matrix
0. Выход
Ваш выбор: > """

TRANSPONSE = """
1. Главная диагональ
2. Side diagonal
3. Вертикальной линии
4. Горизонтальной линии
Ваш выбор: > """


class Matrix:

    def __init__(self, rows=None, columns=None, number=""):
        """
        Класс для создания матрицы
        :param rows: количество строк
        :param columns: количество колонок
        :param number: номер матрицы
        """
        self.matrix = False
        self.__rows = 0
        self.__columns = 0

        try:
            if rows and columns:
                self.__rows = rows
                self.__columns = columns
                self.matrix = [[0] * self.columns for _ in range(self.rows)]
            else:
                rows, columns = input(f"Введите размер(количество и размер строк) {number}матрицы, через пробел: > ") \
                    .split()
                self.rows = int(rows)
                self.columns = int(columns)
        except (ValueError, TypeError):
            print("Ожидается два значения")
        else:
            if not rows and not columns:
                self.matrix = self.init_matrix(number)

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

    def multiply_const_matrix(self):
        """
        Умножение матрицы на число
        :return: Новую матрицу
        """
        try:
            const = input("Введите константу(множитель): > ")
            const = float(const) if "." in const else int(const)
            matrix = [[const * column for column in row] for row in self.matrix]
            return matrix
        except (ValueError, TypeError):
            print("Ожидается число")

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
        inverse = Matrix(rows=self.rows, columns=self.rows)
        inverse.matrix = self.cofactor_matrix()
        inverse.matrix = inverse.transposition_main_diagonal()
        inverse.matrix = [[int(det * column * 100) / 100 for column in row] for row in inverse.matrix]
        return inverse.matrix


def add_matrices(A: Matrix, B: Matrix):
    matrix = list()
    for row in range(A.rows):
        matrix.append([])
        for column in range(A.columns):
            matrix[row].append(A.matrix[row][column] + B.matrix[row][column])
    # matrix = [[(A.matrix[n][m] + B.matrix[n][m]) for m in range(A.column)] for n in range(A.row)]
    return matrix


def multiply_matrices(A: Matrix, B: Matrix):
    matrix = list()
    for k in range(A.rows):
        matrix.append([])
        for m in range(B.columns):
            c = 0
            for n in range(B.rows):
                c += A.matrix[k][n] * B.matrix[n][m]
            matrix[k].append(c)
    return matrix


def print_matrix(matrix):
    if matrix:
        print("Результирующая матрица:")
        for row in matrix:
            print(' '.join([str(elem) for elem in row]))
    else:
        print("Попробуйте ещё раз.")


def transpose_matrix():
    new_choice = input(TRANSPONSE)
    A = Matrix()
    if A.matrix:
        if new_choice == "1":
            print_matrix(A.transposition_main_diagonal())
        if new_choice == "2":
            print_matrix(A.transposition_side_diagonal())
        if new_choice == "3":
            print_matrix(A.transposition_vertical_line())
        if new_choice == "4":
            print_matrix(A.transposition_horizontal_line())
    else:
        print("Операция не может быть выполнена.")


def main():
    while True:
        choice = input(MENU)
        if choice == "0":
            break
        elif choice == "1" or choice == "3":
            A = Matrix(number="первой ")
            B = Matrix(number="второй ")
            if A.matrix and B.matrix:
                if choice == "1" and A.rows == B.rows and A.columns == B.columns:
                    print_matrix(add_matrices(A, B))
                elif choice == "3" and A.columns == B.rows:
                    print_matrix(multiply_matrices(A, B))
                else:
                    print("Операция не может быть выполнена.")
            else:
                print("Матрицы не были инициализированы.")
        elif choice == "2" or choice == "5" or choice == "6":
            A = Matrix()
            if A.matrix:
                if choice == "2":
                    print_matrix(A.multiply_const_matrix())
                elif choice == "5" and A.rows == A.columns:
                    det = A.calculate_determinant(A.matrix, A.rows)
                    print(f"Детерминант матрицы:\n{det}")
                elif choice == "6" and A.rows == A.columns:
                    det = A.calculate_determinant(A.matrix, A.rows)
                    if det != 0:
                        print_matrix(A.inverse_matrix(det))
                    else:
                        print("This matrix doesn't have an inverse.")
                else:
                    print("Операция не может быть выполнена.")
            else:
                print("Матрица не была инициализирована.")
        elif choice == "4":
            transpose_matrix()
        else:
            print("Неверный выбор. Попробуйте ещё раз.")


if __name__ == "__main__":
    # main()
    print(Matrix.__doc__)
