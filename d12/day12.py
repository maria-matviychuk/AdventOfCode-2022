from day12_input import DATA

test_input = """
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
"""


def is_allowed(new_value, old_value):
    if old_value == 'S' and new_value in 'ab':
        return True
    if new_value == 'E' and old_value not in 'yz':
        return False
    if old_value == 'E':
        return False

    next_allowed = chr(ord(old_value) + 1)
    return ord(new_value) <= ord(next_allowed)


def first_res(data):
    matrix = []

    counter = 0
    start_position = 0, 0
    end_position = 0, 0
    for line in data.strip().splitlines():
        matrix.append(list(line))
        if 'S' in line:
            start_position = counter, line.index('S')
        if 'E' in line:
            end_position = counter, line.index('E')
        counter += 1

    step = 1
    wave = []
    visited = dict()
    wave.append(start_position)
    visited[start_position] = 0

    while wave:
        new_wave = []

        for i, j in wave:
            for n_i, n_j in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if not 0 <= n_i < len(matrix):
                    continue
                if not 0 <= n_j < len(matrix[0]):
                    continue
                if (n_i, n_j) in visited:
                    continue
                if not is_allowed(matrix[n_i][n_j], matrix[i][j]):
                    continue
                new_wave.append((n_i, n_j))
                visited[(n_i, n_j)] = step
        step += 1
        wave = new_wave

    return visited.get(end_position)


def is_allowed_backwards(new_value, old_value):
    if old_value == 'E':
        return new_value in 'yz'
    if new_value == 'S':
        return old_value in 'ab'
    if old_value == 'S':
        return False

    next_allowed = chr(ord(old_value) - 1)
    return ord(new_value) >= ord(next_allowed)


def second_res(data):
    matrix = []

    counter = 0
    end_position = 0, 0
    for line in data.strip().splitlines():
        matrix.append(list(line))
        if 'E' in line:
            end_position = counter, line.index('E')
        counter += 1

    wave = [end_position]
    step = 1
    seen = dict()

    first_a = 0
    while wave:
        new_wave = []

        for i, j in wave:
            for n_i, n_j in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if not 0 <= n_i < len(matrix):
                    continue
                if not 0 <= n_j < len(matrix[0]):
                    continue
                if (n_i, n_j) in seen:
                    continue
                if not is_allowed_backwards(matrix[n_i][n_j], matrix[i][j]):
                    continue
                new_wave.append((n_i, n_j))
                if matrix[n_i][n_j] == 'a' and first_a == 0:
                    first_a = step
                seen[(n_i, n_j)] = step

        step += 1
        wave = new_wave

    return first_a


assert first_res(test_input) == 31
assert first_res(DATA) == 520
assert second_res(test_input) == 29
assert second_res(DATA) == 508
