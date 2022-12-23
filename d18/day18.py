from copy import copy

from d18.day18_input import DATA

test_input = """
2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5
"""


def read_data(data):
    cubes = []
    for line in data.strip().splitlines():
        cubes.append([int(l) for l in line.split(',')])
    return cubes


def inner_area(cubes):
    total_area = len(cubes) * 6

    for x,y,z in cubes:
        for x2, y2, z2 in cubes:
            if x == x2 and y == y2 and z == z2:
                continue

            if (x == x2 and y == y2 and abs(z - z2) == 1) or \
                    (y == y2 and z == z2 and abs(x - x2) == 1) or \
                    (x == x2 and z == z2 and abs(y - y2) == 1):
                total_area -= 1
    return total_area


def first_res(data):
    cubes = read_data(data)
    return inner_area(cubes)


def second_res(data):
    cubes = read_data(data)

    max_x = max([x for x,y,z in cubes]) + 1
    min_x = min([x for x,y,z in cubes]) - 1

    max_y = max([y for x,y,z in cubes]) + 1
    min_y = min([y for x,y,z in cubes]) - 1

    max_z = max([z for x,y,z in cubes]) + 1
    min_z = min([z for x,y,z in cubes]) - 1

    wave = []
    water = set()
    wave.append((min_x, min_y, min_z))
    while wave:
        new_wave = []

        for i, j, k in wave:
            if (i, j, k) in water:
                continue
            water.add((i, j, k))
            for n_i, n_j, n_k in ((i + 1, j, k), (i - 1, j, k), (i, j + 1, k), (i, j - 1, k), (i, j, k + 1), (i, j, k - 1)):
                if not min_x <= n_i <= max_x:
                    continue
                if not min_y <= n_j <= max_y:
                    continue
                if not min_z <= n_k <= max_z:
                    continue
                if (n_i, n_j, n_k) in water:
                    continue
                if [n_i, n_j, n_k] in cubes:
                    continue
                new_wave.append((n_i, n_j, n_k))
        wave = new_wave

    lava = {
        (x, y, z)
        for x in range(min_x, max_x + 1)
        for y in range(min_y, max_y + 1)
        for z in range(min_z, max_z + 1)
        if (x, y, z) not in water
    }

    res = 0
    for i, j, k in lava:
        for n_i, n_j, n_k in ((i + 1, j, k), (i - 1, j, k), (i, j + 1, k), (i, j - 1, k), (i, j, k + 1), (i, j, k - 1)):
            if (n_i, n_j, n_k) not in lava:
                res += 1

    return res


assert first_res(test_input) == 64
assert first_res(DATA) == 3448

assert second_res(test_input) == 58
assert second_res(DATA) == 2052
