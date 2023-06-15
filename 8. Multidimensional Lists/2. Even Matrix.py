rows = int(input())
# cols = [int(x) for x in input().split(", ")]
matrix = [[int(x) for x in input().split(", ")] for row in range(rows)]
even_matrix = []
for row in matrix:
    for num in row:
        if num % 2 == 0:
            num = [num]
            even_matrix.append(num)
print(matrix)
print(even_matrix)