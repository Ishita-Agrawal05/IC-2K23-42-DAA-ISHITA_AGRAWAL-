def add_matrix(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def subtract_matrix(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def strassen_matrix_multiplication(a, b):
    n = len(a)
    if n == 1:
        return [[a[0][0] * b[0][0]]]

    half = n // 2
    a11 = [row[:half] for row in a[:half]]
    a12 = [row[half:] for row in a[:half]]
    a21 = [row[:half] for row in a[half:]]
    a22 = [row[half:] for row in a[half:]]

    b11 = [row[:half] for row in b[:half]]
    b12 = [row[half:] for row in b[:half]]
    b21 = [row[:half] for row in b[half:]]
    b22 = [row[half:] for row in b[half:]]

    m1 = strassen_matrix_multiplication(add_matrix(a11, a22), add_matrix(b11, b22))
    m2 = strassen_matrix_multiplication(add_matrix(a21, a22), b11)
    m3 = strassen_matrix_multiplication(a11, subtract_matrix(b12, b22))
    m4 = strassen_matrix_multiplication(a22, subtract_matrix(b21, b11))
    m5 = strassen_matrix_multiplication(add_matrix(a11, a12), b22)
    m6 = strassen_matrix_multiplication(subtract_matrix(a21, a11), add_matrix(b11, b12))
    m7 = strassen_matrix_multiplication(subtract_matrix(a12, a22), add_matrix(b21, b22))

    c11 = add_matrix(subtract_matrix(add_matrix(m1, m4), m5), m7)
    c12 = add_matrix(m3, m5)
    c21 = add_matrix(m2, m4)
    c22 = add_matrix(subtract_matrix(add_matrix(m1, m3), m2), m6)

    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(half):
        for j in range(half):
            result[i][j] = c11[i][j]
            result[i][j + half] = c12[i][j]
            result[i + half][j] = c21[i][j]
            result[i + half][j + half] = c22[i][j]

    return result


def main():
    matrix_a = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16],
    ]
    matrix_b = [
        [1, 0, 2, 0],
        [0, 1, 0, 2],
        [3, 0, 4, 0],
        [0, 3, 0, 4],
    ]
    result = strassen_matrix_multiplication(matrix_a, matrix_b)
    for row in result:
        print(row)


if __name__ == "__main__":
    main()
