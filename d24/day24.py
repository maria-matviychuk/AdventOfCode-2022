from d24.day24_input import DATA

test_input = """
#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#
"""


def read_data(data):
    matrix = []
    for line in data.strip().splitlines():
        matrix.append(list(line))

    length = len(matrix)
    width = len(matrix[0])

    blizzards = []
    for i in range(length):
        for j in range(width):
            if matrix[i][j] in '<>^v':
                blizzards.append((i, j, matrix[i][j]))
    return matrix, blizzards, length, width


def blizzard_move(x, y, dx, dy, width, height):
    return (x + dx) % height, (y + dy) % width


directions = {
    '>': (0,1),
    'v': (1,0),
    '<': (0,-1),
    '^': (-1,0)
}


def move_blizzards(blizzards, width, height, matrix):
    new_blizzards = []
    for i, j, direction in blizzards:
        dx, dy = directions[direction]

        n_i, n_j = blizzard_move(i, j, dx, dy, width, height)
        while matrix[n_i][n_j] == '#':
            n_i, n_j = blizzard_move(n_i, n_j, dx, dy, width, height)

        new_blizzards.append((n_i, n_j, direction))
    return new_blizzards

def make_round(start_i, start_j, matrix, width, height, blizzards, end_i, end_j):
    step = 0
    wave = set()
    wave.add((start_i, start_j))
    while wave:
        new_wave = set()

        blizzards = move_blizzards(blizzards, width, height, matrix)
        blizzards_coordinates = [(x, y) for x, y, z in blizzards]

        for i, j in wave:
            for n_i, n_j in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1), (i, j)):
                if not 0 <= n_i < len(matrix):
                    continue
                if not 0 <= n_j < len(matrix[0]):
                    continue
                if (n_i, n_j) in blizzards_coordinates:
                    continue
                if matrix[n_i][n_j] == '#':
                    continue
                new_wave.add((n_i, n_j))
        step += 1

        if (end_i, end_j) in new_wave:
            break

        wave = new_wave

    return step, blizzards


def first_res(data):
    matrix, blizzards, length, width = read_data(data)
    start_i, start_j = 0, 1
    end_i, end_j = length - 1, width -2
    steps, blizzards = make_round(start_i, start_j, matrix, width, length, blizzards, end_i, end_j)
    return steps


def second_res(data):
    matrix, blizzards, length, width = read_data(data)
    start_i, start_j = 0, 1
    end_i, end_j = length - 1, width - 2
    steps, blizzards = make_round(start_i, start_j, matrix, width, length, blizzards, end_i, end_j)
    steps2, blizzards = make_round(end_i, end_j, matrix, width, length, blizzards, start_i, start_j)
    steps3, blizzards = make_round(start_i, start_j, matrix, width, length, blizzards, end_i, end_j)
    return steps + steps2 + steps3


assert first_res(test_input) == 18
assert first_res(DATA) == 288

assert second_res(test_input) == 54
assert second_res(DATA) == 861
