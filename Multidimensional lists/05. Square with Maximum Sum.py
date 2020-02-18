def read_matrix(matrix_size):
    matrix = []
    rows = matrix_size[0]
    columns = matrix_size[1]
    for row in range(rows):
        current = list(map(int, input().split(", ")))
        matrix.append(current)
    return matrix


def best_sum(matrix):
    row_counts = len(matrix)
    col_counts = len(matrix[0])
    best_sum = None
    best_start = None
    for row in range(row_counts - 1):
        for col in range(col_counts - 1):
            sum_2_2 = matrix[row][col] + matrix[row][col + 1] + matrix[row + 1][col] + matrix[row + 1][col + 1]
            if best_sum:
                if best_sum < sum_2_2:
                    best_sum = sum_2_2
                    best_start = (row, col)
            else:
                best_sum = sum_2_2
                best_start = (row, col)

    return  best_sum, best_start


def get_mini_matrix(matrix, start_index):
    m_matrix = []
    start_row = start_index[0]
    start_col = start_index[1]
    first_row = [matrix[start_row][start_col], matrix[start_row][start_col + 1]]
    second_row = [matrix[start_row + 1][start_col], matrix[start_row + 1][start_col + 1]]
    m_matrix.append(first_row)
    m_matrix.append(second_row)
    return m_matrix


matrix_size = list(map(int, input().split(", ")))

matrix = read_matrix(matrix_size)
b_sum, b_start = best_sum(matrix)
get_mini_matrix = get_mini_matrix(matrix, b_start)
#print(get_mini_matrix)
for i in range(len(get_mini_matrix)):
    current = list(map(str, get_mini_matrix[i]))
    print(" ".join(current))
#print(get_mini_matrix)
print(b_sum)
# print(b_start)









