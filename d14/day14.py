from d14.day14_input import DATA

test_input = """
498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
"""


def fall(sand_x, sand_y, matrix, sand, min_x, max_x, is_break=True):
    if is_break and (sand_y <= min_x or sand_y > max_x):
        raise

    if matrix[sand_x + 1][sand_y] == '.':
        return fall(sand_x + 1, sand_y, matrix, sand, min_x, max_x, is_break)

    if matrix[sand_x + 1][sand_y] not in ['.']:
        if sand_y - 1 > 0 and matrix[sand_x + 1][sand_y - 1] == '.':
            return fall(sand_x + 1, sand_y - 1, matrix, sand, min_x, max_x, is_break)
        elif sand_y + 1 < len(matrix[0]) and matrix[sand_x + 1][sand_y + 1] == '.':
            return fall(sand_x + 1, sand_y + 1, matrix, sand, min_x, max_x, is_break)
        else:
            sand.append((sand_x, sand_y))
            matrix[sand_x][sand_y] = 'o'
            return

    if matrix[sand_x + 1][sand_y] == '#':
        sand.append((sand_x, sand_y))
        matrix[sand_x][sand_y] = 'o'
        return


def read_data(data, sand_source):
    max_x = sand_source
    min_x = sand_source
    max_y = 0

    matrix = [['.'] * sand_source * 2 for i in range(200)]

    for line in data.strip().splitlines():
        path = []
        coords = line.split(" -> ")
        for coord in coords:
            x, y = (int(k) for k in coord.split(','))
            path.append((x, y))
            if x > max_x:
                max_x = x
            if x < min_x:
                min_x = x
            if y > max_y:
                max_y = y

        start_x, start_y = path[0]
        for i in range(1, len(path)):
            end_x, end_y = path[i]
            if start_x == end_x:  # horizontal
                while start_y != end_y:
                    matrix[start_y][start_x] = '#'
                    if start_y < end_y:
                        start_y += 1
                    else:
                        start_y -= 1
                matrix[start_y][start_x] = '#'
            elif start_y == end_y:  # vertical
                while start_x != end_x:
                    matrix[start_y][start_x] = '#'
                    if start_x < end_x:
                        start_x += 1
                    else:
                        start_x -= 1
                matrix[start_y][start_x] = '#'
    return matrix, min_x, max_x, max_y


def first_res(data):
    sand_x, sand_y = 0, 500
    sand = []

    matrix, min_x, max_x, max_y = read_data(data, sand_y)
    try:
        while True:
            fall(sand_x, sand_y, matrix, sand, min_x, max_x)
    except:
        pass

    for r in matrix:
        print(r[min_x:max_x])

    print(len(sand))
    return len(sand)


def second_res(data):
    sand_x, sand_y = 0, 500
    sand = []

    matrix, min_x, max_x, max_y = read_data(data, sand_y)
    matrix[max_y + 2] = ['#'] * 1000

    while True:
        fall(sand_x, sand_y, matrix, sand, min_x, max_x, is_break=False)
        if (sand_x, sand_y) in sand:
            break

    for r in matrix[:max_y + 3]:
        print(r)

    print(len(sand))
    return len(sand)


assert first_res(test_input) == 24
assert first_res(DATA) == 888

assert second_res(test_input) == 93
assert second_res(DATA) == 26461
