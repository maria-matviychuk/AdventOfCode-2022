from d22.day22_input import DATA

test_input = """
        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5
"""


def read_data(data):
    tiles = []
    max_width = 0
    moves = data.rstrip().splitlines()[-1]
    lines = data.rstrip().splitlines()[:-2]
    for line in lines:
        if len(line.strip()) > 0:
            tiles.append(list(line))
        if len(line) > max_width:
            max_width = len(line)

    for line in tiles:
        if len(line) < max_width:
            diff = max_width - len(line)
            dif_l = []
            dif_l[:]  = [' '] * diff
            line.extend(dif_l)
    return tiles, moves, max_width


def rotate(initial_direction, clockwise=True):
    a = 1 if clockwise else -1
    possible = ['R', 'D', 'L', 'U']
    new_index = possible.index(initial_direction) + a
    return possible[new_index % len(possible)]


def iterate_moves(moves, direction):
    while True:
        l, r = 0, 0
        if 'L' in moves:
            l = moves.index('L')
        if 'R' in moves:
            r = moves.index('R')
        if 0 < l < r or (r == 0 and 0 < l):
            index = l
            yield int(moves[:l]), direction
            direction = rotate(direction, False)
        elif 0 < r < l or (l == 0 and 0 < r):
            index = r
            yield int(moves[:r]), direction
            direction = rotate(direction, True)
        else:
            yield int(moves), direction
            break

        moves = moves[index + 1:]


def get_to_other_side(line):
    if '.' not in line:
        return

    start_dot = line.index('.')
    if '#' in line:
        start_wall = line.index('#')
        if start_wall < start_dot:
            return
    return start_dot


def move(x, y, dx, dy, width, height):
    return (x + dx) % width, (y + dy) % height


def first_res(data):
    tiles, moves, max_width = read_data(data)

    directions = {
        'R': (0,1),
        'D': (1,0),
        'L': (0,-1),
        'U': (-1,0)
    }

    arrows = {
        'R': '>',
        'D': 'V',
        'L': '<',
        'U': '^'
    }

    start_x, start_y = 0, tiles[0].index('.')

    for count, direction in iterate_moves(moves, 'R'):
        tiles[start_x][start_y] = arrows[direction]
        for i in range(0, count):
            dir_x, dir_y = directions[direction]
            n_x, n_y = move(start_x, start_y, dir_x, dir_y, len(tiles), len(tiles[0]))

            while tiles[n_x][n_y] == ' ':
                n_x, n_y = move(n_x, n_y, dir_x, dir_y, len(tiles), len(tiles[0]))

            if tiles[n_x][n_y] == '#':
                break
            else:
                start_x, start_y = n_x, n_y
            tiles[start_x][start_y] = arrows[direction]

    facing = {'>': 0, 'v': 1, '<': 2,  '^': 3}.get(tiles[start_x][start_y])
    return facing + (start_y + 1) * 4 + (start_x + 1) * 1000


def second_res(data):
    pass


assert first_res(test_input) == 6032
assert first_res(DATA) == 106094
#
# assert second_res(test_input) == 1
# assert second_res(DATA) == 1