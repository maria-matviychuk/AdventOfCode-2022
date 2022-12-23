from d15.day15_input import DATA

test_input = """
Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3
"""


def read_data(data):
    tmp = dict()
    for line in data.strip().splitlines():
        sensor, beacon = line.split(':')
        sx, sy = sensor.split('=')[1], sensor.split('=')[2]
        bx, by = beacon.split('=')[1], beacon.split('=')[2]
        sx = sx.replace(', y', '')
        bx = bx.replace(', y', '')
        tmp[(int(sx), int(sy))] = (int(bx), int(by))
    return tmp


def proceed(sx, sy, bx, by, row_target, inputs, res):
    distance = abs(bx - sx) + abs(by - sy)

    if sy - distance > row_target or sy + distance < row_target:
        return

    if sy < row_target:
        diff = row_target - sy
    else:
        diff = sy - row_target

    amount_x = distance - diff
    while amount_x >= 0:
        for sx_n in (sx + amount_x, sx - amount_x):
            if (sx_n, row_target) not in inputs.keys() and (sx_n, row_target) not in inputs.values():
                res.add(sx_n)
        amount_x -= 1


def first_res(data, row_target=2000000):
    res = set()
    inputs = read_data(data)

    for key, value in inputs.items():
        sx, sy = key
        bx, by = value
        proceed(sx, sy, bx, by, row_target, inputs, res)

    return len(res)


def find_possible_position(sx, sy, bx, by, possible_positions, max_value):
    distance = abs(bx - sx) + abs(by - sy) + 1
    diff = 0
    while distance != 0:
        for sx_n in (sx + distance, sx - distance):
            for sy_n in (sy + diff, sy - diff):
                if max_value >= sx_n >= 0 and max_value >= sy_n >= 0:
                    possible_positions.add((sx_n, sy_n))
        diff += 1
        distance -= 1


def check_distance(sx, sy, bx, by, x, y):
    distance = abs(bx - sx) + abs(by - sy)
    distance2 = abs(x - sx) + abs(y - sy)
    return distance2 > distance


def second_res(data, max_coord):
    inputs = read_data(data)

    possible = set()
    for key, value in inputs.items():
        sx, sy = key
        bx, by = value
        find_possible_position(sx, sy, bx, by, possible, max_coord)

    found_y, found_x, found = 0, 0, False
    for x, y in possible:
        for key, value in inputs.items():
            sx, sy = key
            bx, by = value
            if not check_distance(sx, sy, bx, by, x, y):
                break
        else:
            found = True
            found_x = x
            found_y = y

        if found:
            break

    return found_x * 4000000 + found_y


assert first_res(test_input, 10) == 26
assert first_res(DATA, 2000000) == 4725496

assert second_res(test_input, 20) == 56000011
assert second_res(DATA, 4000000) == 12051287042458
