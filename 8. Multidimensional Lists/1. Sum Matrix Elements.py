rows, cols = [int(x) for x in input().split(", ")]
matrix = [[int(x) for x in input().split(", ")] for row in range(rows)]
sum = 0
for s in matrix:
    for x in s:
        x = int(x)
        sum += x
print(sum)
print(matrix)

