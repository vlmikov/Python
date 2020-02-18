def sum_primary_diagonal(matrix):
    the_sum = 0
    rows = len(matrix)
    for r in range(rows):
        the_sum += matrix[r][r]
    return the_sum


def read_matrix(size):
    matrix = []
    rows = size
    for r in range(rows):
        current = list(map(int, input().split(" ")))
        matrix.append(current)
    return matrix





size = int(input())

matrix = read_matrix(size)
print(sum_primary_diagonal(matrix))
