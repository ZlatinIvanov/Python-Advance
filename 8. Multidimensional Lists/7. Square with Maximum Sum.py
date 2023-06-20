def find_max_submatrix(matrix):
    max_sum = float('-inf')
    max_submatrix = []

    for i in range(len(matrix) - 1):
        for j in range(len(matrix[i]) - 1):
            submatrix_sum = matrix[i][j] + matrix[i][j+1] + matrix[i+1][j] + matrix[i+1][j+1]
            if submatrix_sum > max_sum:
                max_sum = submatrix_sum
                max_submatrix = [[matrix[i][j], matrix[i][j+1]], [matrix[i+1][j], matrix[i+1][j+1]]]

    return max_submatrix, max_sum

size = input()
rows, columns = map(int, size.split(','))

matrix = []
for _ in range(rows):
    row = input()
    row_elements = list(map(int, row.split(', ')))
    matrix.append(row_elements)

max_submatrix, max_sum = find_max_submatrix(matrix)

for row in max_submatrix:
    print(' '.join(str(element) for element in row))
print(max_sum)
