def multi(m1: list, m2: list) -> list:
    n = len(m1[0])
    # verifica se m1.columns = m2.rows
    if (n != len(m2)):
        raise Exception('A.columns != B.rows')

    rows = len(m1)
    cols = len(m2[0])
    m3 = [[0 for x in range(cols)] for y in range(rows)]

    for i in range(rows):
        for j in range(cols):
            for k in range(n):
                m3[i][j] = m3[i][j] + m1[i][k] * m2[k][j]

    return m3


def _print_matrix(matrix: list) -> list:
    output = ''
    for i in range(len(matrix)):
        output += f'[{matrix[i][0]}'
        for j in range(1, len(matrix[i])):
            output += f',{matrix[i][j]}'
        output += ']'
        if (i != len(matrix) - 1):
            output += '\n'
    print(output)


if __name__ == "__main__":
    matrix_A = [[0 for x in range(2)] for y in range(3)] #first columns and second is rows
    matrix_A[0][0] = 3
    matrix_A[1][0] = 2
    matrix_A[2][0] = 0
    matrix_A[0][1] = 1
    matrix_A[1][1] = -1
    matrix_A[2][1] = 4

    matrix_B = [[0 for x in range(3)] for y in range(2)]
    matrix_B[0][0] = 1
    matrix_B[0][1] = -1
    matrix_B[0][2] = 2
    matrix_B[1][0] = 3
    matrix_B[1][1] = 0
    matrix_B[1][2] = 5

    print('Matriz A:')
    _print_matrix(matrix_A)
    print('Matriz B:')
    _print_matrix(matrix_B)
    print('Multi A X B')
    result = multi(matrix_A, matrix_B)
    _print_matrix(result)
