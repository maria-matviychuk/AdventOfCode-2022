from collections import defaultdict

from d23.day23_input import DATA

test_input = """
....#..
..###.#
#...#.#
.#...##
#.###..
##.#.##
.#..#..
"""


def read_data(data):
    matrix = []
    for line in data.strip().splitlines():
        matrix.append(list(line))
    return matrix


NORTH = [
    (-1, 0),
    (-1, -1),
    (-1, 1),
]


SOUTH =[
    (1, 0),
    (1, -1),
    (1, 1),
]

WEST = [
    (0, 1),
    (-1, 1),
    (1, 1),
]

EAST = [
    (0, -1),
    (1, -1),
    (-1, -1),
]

DIRECTIONS = [
    (-1, 0),
    (-1, -1),
    (-1, 1),
    (1, 0),
    (1, -1),
    (1, 1),
    (0, 1),
    (-1, 1),
    (1, 1),
    (0, -1),
    (1, -1),
    (-1, -1),
]


order = [NORTH,SOUTH, EAST, WEST]

def is_move(x, y, matrix):
    return not all([matrix[x + i][y + j] == '.' for i, j in DIRECTIONS])


def can_move_in_direction(x, y, matrix, direction_coordinates):
    return all([matrix[x + i][y + j] == '.' for i, j in direction_coordinates])


def extend_matrix(matrix):
    width = len(matrix[0])
    if '#' in matrix[0]:
        matrix.insert(0, ['.'] * width)
    if '#' in matrix[-1]:
        matrix.append(['.'] * width)

    if any(line[0] == '#' for line in matrix):
        for line in matrix:
            line.insert(0, '.')

    if any(line[-1] == '#' for line in matrix):
        for line in matrix:
            line.append('.')


def movements(matrix, first_direction, check_no_move=False):
    extend_matrix(matrix)

    considered_movements = defaultdict(list)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == '#':
                if is_move(i, j, matrix):
                    for count in range(len(order)):
                        direction = (first_direction + count) % len(order)
                        direction_coordinates = order[direction]
                        if can_move_in_direction(i, j, matrix, direction_coordinates):
                            dx, dy = direction_coordinates[0]
                            considered_movements[(i + dx, j + dy)].append((i, j))
                            break

    if check_no_move and len(considered_movements) == 0:
        return None

    for key, value in considered_movements.items():
        if len(value) > 1:
            considered_movements[key] = []

    for key, value in considered_movements.items():
        if len(value) == 0:
            continue
        old_i, old_j = value[0]
        n_i, n_j = key
        matrix[old_i][old_j] = '.'
        matrix[n_i][n_j] = '#'

    return first_direction + 1


def first_res(data):
    matrix = read_data(data)
    first_direction = 0
    for i in range(0, 10):
        first_direction = movements(matrix, first_direction)

    min_i, min_j, max_i, max_j = 0, 0, 0, 0
    for i in range(len(matrix)):
        if '#' in matrix[i]:
            if min_i == 0:
                min_i = i
            if i > max_i:
                max_i = i

            for j in range(len(matrix[i])):
                if matrix[i][j] == '#':
                    if min_j == 0 or min_j > j:
                        min_j = j
                    if j > max_j:
                        max_j = j

    res = 0
    for i in range(min_i, max_i + 1):
        for j in range(min_j, max_j + 1):
            if matrix[i][j] == '.':
                res += 1

    return res

def second_res(data):
    matrix = read_data(data)
    first_direction = 0
    counter = 0
    while True:
        first_direction = movements(matrix, first_direction, check_no_move=True)
        counter += 1
        if first_direction is None:
            break
    return counter


assert first_res(test_input) == 110
assert first_res(DATA) == 3906

assert second_res(test_input) == 20
assert second_res(DATA) == 895
