def filter_even_numbers(matrix):
    even_matrix = [[num for num in row if num % 2 == 0] for row in matrix]
    return even_matrix

rows = int(input())

matrix = []

for _ in range(rows):
    row = [int(num) for num in input().split(", ")]
    matrix.append(row)

even_matrix = filter_even_numbers(matrix)

print(even_matrix)
