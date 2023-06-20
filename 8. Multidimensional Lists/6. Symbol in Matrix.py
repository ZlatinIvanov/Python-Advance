def find_symbol(matrix, symbol):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == symbol:
                return f"({i}, {j})"
    return f"{symbol} does not occur in the matrix"


n = int(input())

matrix = []
for _ in range(n):
    row = input()
    matrix.append(list(row))

symbol = input()

result = find_symbol(matrix, symbol)

print(result)
