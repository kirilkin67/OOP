class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = [[0] * cols for _ in range(rows)]

    def __str__(self):
        return 'Матрица:\n' + '\n'.join([' '.join(map(str, row)) for row in self.matrix])

    def __getitem__(self, indices):
        row, col = indices
        return self.matrix[row][col]

    def __setitem__(self, indices, value):
        row, col = indices
        self.matrix[row][col] = value

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions")
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result[i, j] = self[i, j] + other[i, j]
        return result

    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions")
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result[i, j] = self[i, j] - other[i, j]
        return result

    def __mul__(self, scalar):
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result[i, j] = self[i, j] * scalar
        return result

    def multiply(self, other):
        if self.cols != other.rows:
            raise ValueError(
                "Number of columns in the first matrix must be equal to the number of rows in the second matrix")
        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result[i, j] += self[i, k] * other[k, j]
        return result


if __name__ == "__main__":
    m1 = Matrix(2, 3)
    m1[0, 0] = 1
    m1[0, 1] = 2
    m1[0, 2] = 3
    m1[1, 0] = 4
    m1[1, 1] = 5
    m1[1, 2] = 6

    m2 = Matrix(3, 2)
    m2[0, 0] = 7
    m2[0, 1] = 8
    m2[1, 0] = 9
    m2[1, 1] = 10
    m2[2, 0] = 11
    m2[2, 1] = 12

    print(m1)  # Output: 1 2 3 \n 4 5 6
    print(m2)  # Output: 7 8 \n 9 10 \n 11 12

    # print(m1 + m2)  # Output: 8 10  \n 13 15
    # print(m1 - m2)  # Output: -6 -6 \n -5 -5
    print(m1 * 2)   # Output: 2 4 6 \n 8 10 12

    m3 = m1.multiply(m2)
    print(m3)  # Output: 58 64 \n 139 154