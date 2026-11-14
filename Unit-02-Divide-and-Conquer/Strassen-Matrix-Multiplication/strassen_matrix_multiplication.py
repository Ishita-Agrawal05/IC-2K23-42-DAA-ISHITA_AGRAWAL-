"""Strassen matrix multiplication for square matrices with sizes that are powers of two."""

def add_matrix(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def subtract_matrix(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def strassen_mul(a, b):
    n = len(a)
    if n == 1:
        return [[a[0][0] * b[0][0]]]

    mid = n // 2
    a11 = [row[:mid] for row in a[:mid]]
    a12 = [row[mid:] for row in a[:mid]]
    a21 = [row[:mid] for row in a[mid:]]
    a22 = [row[mid:] for row in a[mid:]]

    b11 = [row[:mid] for row in b[:mid]]
    b12 = [row[mid:] for row in b[:mid]]
    b21 = [row[:mid] for row in b[mid:]]
    b22 = [row[mid:] for row in b[mid:]]

    m1 = strassen_mul(add_matrix(a11, a22), add_matrix(b11, b22))
    m2 = strassen_mul(add_matrix(a21, a22), b11)
    m3 = strassen_mul(a11, subtract_matrix(b12, b22))
    m4 = strassen_mul(a22, subtract_matrix(b21, b11))
    m5 = strassen_mul(add_matrix(a11, a12), b22)
    m6 = strassen_mul(subtract_matrix(a21, a11), add_matrix(b11, b12))
    m7 = strassen_mul(subtract_matrix(a12, a22), add_matrix(b21, b22))

    c11 = add_matrix(subtract_matrix(add_matrix(m1, m4), m5), m7)
    c12 = add_matrix(m3, m5)
    c21 = add_matrix(m2, m4)
    c22 = add_matrix(subtract_matrix(add_matrix(m1, m3), m2), m6)

    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(mid):
        for j in range(mid):
            result[i][j] = c11[i][j]
            result[i][j + mid] = c12[i][j]
            result[i + mid][j] = c21[i][j]
            result[i + mid][j + mid] = c22[i][j]
    return result


def main():
    matrix_a = [[1, 2], [3, 4]]
    matrix_b = [[5, 6], [7, 8]]
    product = strassen_mul(matrix_a, matrix_b)
    print("Matrix A:", matrix_a)
    print("Matrix B:", matrix_b)
    print("Product:", product)


if __name__ == "__main__":
    main()
