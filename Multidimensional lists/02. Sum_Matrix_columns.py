def read_matrix(num_rows):
    matrix = []
    for row in range(num_rows):
        current_row = list(map(int, input().split(" ")))
        matrix.append(current_row)
    return matrix

def sum_of_columns(matrix):
    sum_lsit = []
    rows = len(matrix)
    columns = len(matrix[0])
    for column in range(columns):
        the_sum = 0
        for row in range(rows):
            the_sum += int(matrix[row][column])
        sum_lsit.append(the_sum)
    return sum_lsit


rows, columns = map(int, input().split(","))
matrix = read_matrix(rows)

[print(x) for x in sum_of_columns(matrix)]