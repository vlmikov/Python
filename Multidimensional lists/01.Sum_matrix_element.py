def read_matrix(rows, columns):
    matrix = []
    for row in range(rows):
        current_row = list(map(int,input().split(",")))
        matrix.append(current_row)
    return matrix




def sum_matrix(matrix):
    the_sum = 0
    rows_count = len(matrix)
   # cols_count = len(matrix[0])
    for row in range(rows_count):
        the_sum += sum(matrix[row])

    return the_sum



rows, columns = map(int,input().split(","))

# matrix = [
#     [7, 1, 3, 3, 2, 1],
#     [1, 3, 9, 8, 5, 6],
#     [4, 6, 7, 9, 1, 0],
# ]

matrix = read_matrix(rows, columns)
print(sum_matrix(matrix))
print(matrix)