rows, cols = [int(x) for x in input().split(", ")]

matrix = []

for _ in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

column_sums = [sum(column) for column in zip(*matrix)]

for sum_val in column_sums:
    print(sum_val)

