rows = int(input())
sum_diagonals = 0
for i in range(rows):
	sum_diagonals += [int(i) for i in input().split()][i]
print(sum_diagonals)