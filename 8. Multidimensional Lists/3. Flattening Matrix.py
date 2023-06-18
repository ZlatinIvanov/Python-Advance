rows = int(input())

matrix = []

for _ in range(rows):
    row = [int(num) for num in input().split(", ")]
    matrix.append(row)

flattened_list = [num for row in matrix for num in row]

print(flattened_list)
