from matrix import Matrix
from matrix_operation import MatrixOperation

MENU = """
1. Сложение 2 матриц
2. Умножение матрицы на число
3. Умножение матриц
4. Транспонирование матрицы
5. Детерминант матрицы
6. Обратная матрица
0. Выход
Ваш выбор: > """

TRANSPONSE = """
1. Главная диагональ
2. Side diagonal
3. Вертикальной линии
4. Горизонтальной линии
Ваш выбор: > """


def transpose_matrix():
    new_choice = input(TRANSPONSE)
    A = Matrix()
    if A.matrix:
        if new_choice == "1":
            MatrixOperation.print_matrix(A.transposition_main_diagonal())
        if new_choice == "2":
            MatrixOperation.print_matrix(A.transposition_side_diagonal())
        if new_choice == "3":
            MatrixOperation.print_matrix(A.transposition_vertical_line())
        if new_choice == "4":
            MatrixOperation.print_matrix(A.transposition_horizontal_line())
    else:
        print("Операция не может быть выполнена.")


def multiply_const(matrix: Matrix):
    try:
        const = input("Введите константу(множитель): > ")
        const = float(const) if "." in const else int(const)
        matrix.multiply_const_matrix(const).print_matrix()
    except (ValueError, TypeError):
        print("Ожидается число")


def main():
    while True:
        choice = input(MENU)
        if choice == "0":
            break
        elif choice == "1" or choice == "3":
            first = Matrix(number="первой ")
            second = Matrix(number="второй ")
            if first.matrix and second.matrix:
                if choice == "1" and first.rows == second.rows and first.columns == second.columns:
                    MatrixOperation.add_matrices(first, second).print_matrix()
                elif choice == "3" and first.columns == second.rows:
                    MatrixOperation.print_matrix(MatrixOperation.multiply_matrices(first, second))
                else:
                    print("Операция не может быть выполнена.")
            else:
                print("Матрицы не были инициализированы.")
        elif choice == "2" or choice == "5" or choice == "6":
            matrix = Matrix()
            if matrix.matrix:
                if choice == "2":
                    multiply_const(matrix)
                elif choice == "5" and matrix.rows == matrix.columns:
                    det = matrix.calculate_determinant(matrix.matrix, matrix.rows)
                    print(f"Детерминант матрицы:\n{det}")
                elif choice == "6" and matrix.rows == matrix.columns:
                    det = matrix.calculate_determinant(matrix.matrix, matrix.rows)
                    print(f"Детерминант матрицы: {det:0.3f}")
                    if det != 0:
                        inverse = matrix.inverse_matrix(det)
                        inverse.print_matrix()
                        print("Проверка обратной матрицы через умножение")
                        MatrixOperation.print_matrix(MatrixOperation.multiply_matrices(matrix, inverse))
                    else:
                        print(f"Детерминант матрицы равен 0. Эта матрица не имеет обратной.")
                else:
                    print("Операция не может быть выполнена.")
            else:
                print("Матрица не была инициализирована.")
        elif choice == "4":
            transpose_matrix()
        else:
            print("Неверный выбор. Попробуйте ещё раз.")


if __name__ == "__main__":
    main()
