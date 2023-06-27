def find_mouse(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'M':
                return i, j

def print_matrix(matrix):
    for row in matrix:
        print(''.join(row))

def eat_cheese(matrix, i, j):
    matrix[i][j] = '*'

def process_directions(matrix, directions):
    trapped = False
    outside = False
    cheese_count = sum(row.count('C') for row in matrix)
    i, j = find_mouse(matrix)

    for direction in directions:
        if trapped or outside:
            break

        if direction == 'up':
            if i > 0 and matrix[i - 1][j] != '@':
                i -= 1
        elif direction == 'down':
            if i < len(matrix) - 1 and matrix[i + 1][j] != '@':
                i += 1
        elif direction == 'left':
            if j > 0 and matrix[i][j - 1] != '@':
                j -= 1
        elif direction == 'right':
            if j < len(matrix[0]) - 1 and matrix[i][j + 1] != '@':
                j += 1

        if matrix[i][j] == 'C':
            eat_cheese(matrix, i, j)
            cheese_count -= 1

        if matrix[i][j] == 'T':
            trapped = True

        if matrix[i][j] == '@':
            outside = True

    return trapped, outside, cheese_count, i, j

def solve_cupboard_area(area):
    input_lines = area.split('\n')
    dimensions = input_lines[0]
    rows = input_lines[1:-1]
    directions = input_lines[-1].split()

    n, m = [int(x) for x in input().split(", ")]
    matrix = [list(row) for row in rows]

    trapped, outside, cheese_count, i, j = process_directions(matrix, directions)

    if trapped:
        return "Mouse is trapped!"

    if outside:
        return "No more cheese for tonight!"

    if cheese_count == 0:
        return "Happy mouse! All the cheese is eaten, good night!"

    return "Mouse will come back later!\n" + '\n'.join(''.join(row) for row in matrix)


# Example usage:
input_data = '''5,5
**M**
T@@**
CC@**
**@@*
**CC*
left
down
left'''
result = solve_cupboard_area(input_data)
print(result)
