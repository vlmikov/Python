

def read_matrix(n):
    matrix = []
    for row in range(n):
        current = list(input())
        matrix.append(current)
    return matrix

def find_symbol(matrix, symbol):
    in_matrix = False
    for row in range(len(matrix)):
        if symbol in matrix[row]:
            current = matrix[row]
            ind = current.index(symbol)
            in_matrix = True
            return (row, ind)
    if in_matrix == False:
        return (-1, -1)





n = int(input())

matrix = read_matrix(n)

symbol = input()
if find_symbol(matrix, symbol) == (-1,-1):
    print(f"{symbol} does not occur in the matrix")
else:
    print(find_symbol(matrix, symbol))
