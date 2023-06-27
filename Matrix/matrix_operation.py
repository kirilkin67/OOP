from matrix import Matrix


class MatrixOperation:
    @staticmethod
    def add_matrices(first: Matrix, second: Matrix):
        final = Matrix(first.rows, first.columns)
        for row in range(first.rows):
            for column in range(first.columns):
                final.matrix[row][column] = first.matrix[row][column] + second.matrix[row][column]
        return final

    @staticmethod
    def add_matrices_2(matrix_1: Matrix, matrix_2: Matrix):
        return [[(matrix_1.matrix[n][m] + matrix_2.matrix[n][m]) for m in range(matrix_1.columns)] for n in
                range(matrix_1.rows)]

    @staticmethod
    def add_matrices_3(matrix_1: Matrix, matrix_2: Matrix):
        matrix = list()
        for row in range(matrix_1.rows):
            matrix.append([])
            for column in range(matrix_1.columns):
                matrix[row].append(matrix_1.matrix[row][column] + matrix_2.matrix[row][column])
        return matrix

    @staticmethod
    def multiply_matrices(matrix_1: Matrix, matrix_2: Matrix):
        matrix = list()
        for k in range(matrix_1.rows):
            matrix.append([])
            for m in range(matrix_2.columns):
                c = 0
                for n in range(matrix_2.rows):
                    c += matrix_1.matrix[k][n] * matrix_2.matrix[n][m]
                matrix[k].append(c)
        return matrix

    @staticmethod
    def print_matrix(matrix):
        if matrix:
            print("Результирующая матрица:")
            for row in matrix:
                for elem in row:
                    print(f"{elem:>10.2f}", end=" ")
                print()
        else:
            print("Попробуйте ещё раз.")
