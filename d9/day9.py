from d9.day9_input import DATA

test_input1 = """
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""


test_input2 = """
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
"""


def move(h_i, h_j, t_i, t_j):
    return abs(h_i - t_i) > 1 or abs(h_j - t_j) > 1


def move_down(t_i, t_j):
    return t_i, t_j + 1


def move_up(t_i, t_j):
    return t_i, t_j - 1


def move_left(t_i, t_j):
    return t_i - 1, t_j


def move_right(t_i, t_j):
    return t_i + 1, t_j


def move_right_down(t_i, t_j):
    return t_i + 1, t_j + 1


def move_right_up(t_i, t_j):
    return t_i + 1, t_j - 1


def move_left_up(t_i, t_j):
    return t_i - 1, t_j - 1


def move_left_down(t_i, t_j):
    return t_i - 1, t_j + 1


def where_move(h_i, h_j, t_i, t_j):
    if h_j == t_j and h_i > t_i:
        return move_right
    elif h_j == t_j and h_i < t_i:
        return move_left
    elif h_i == t_i and h_j > t_j:
        return move_down
    elif h_i == t_i and h_j < t_j:
        return move_up
    elif h_j > t_j and h_i > t_i:
        return move_right_down
    elif h_j > t_j and h_i < t_i:
        return move_left_down
    elif h_j < t_j and h_i > t_i:
        return move_right_up
    elif h_j < t_j and h_i < t_i:
        return move_left_up


def movement(path, knot_len, h_i, h_j, t_i, t_j, h_start_i, h_start_j, head_direction):
    while h_start_i != h_i or h_start_j != h_j:
        h_start_i, h_start_j = head_direction(h_start_i, h_start_j)

        start_i, start_j = h_start_i, h_start_j
        for count in range(1, knot_len):
            if not move(start_i, start_j, t_i[count], t_j[count]):
                start_i, start_j = t_i[count], t_j[count]
                continue

            direction_func = where_move(start_i, start_j, t_i[count], t_j[count])
            t_i[count], t_j[count] = direction_func(t_i[count], t_j[count])
            if count == knot_len - 1:
                path.add((t_i[count], t_j[count]))

            start_i, start_j = t_i[count], t_j[count]


def solution(data, knot_len):
    path = set()

    h_i, h_j = 100, 100
    t_i = []
    t_j = []

    t_i[:knot_len] = [100] * knot_len
    t_j[:knot_len] = [100] * knot_len

    path.add((100, 100))

    for row in data.strip().splitlines():
        direction, count = row.split(" ")
        count = int(count)
        if direction == "D":
            movement(path, knot_len, h_i, h_j + count, t_i, t_j, h_i, h_j, move_down)
            h_j = h_j + count
        elif direction == "U":
            movement(path, knot_len, h_i, h_j - count, t_i, t_j, h_i, h_j, move_up)
            h_j = h_j - count
        elif direction == "L":
            movement(path, knot_len, h_i - count, h_j, t_i, t_j, h_i, h_j, move_left)
            h_i = h_i - count
        elif direction == "R":
            movement(path, knot_len, h_i + count, h_j, t_i, t_j, h_i, h_j, move_right)
            h_i = h_i + count

    return len(path)


def first_res(data):
    return solution(data, 2)


def second_res(data):
    return solution(data, 10)


assert first_res(test_input1) == 13
assert first_res(DATA) == 6311

assert second_res(test_input2) == 36
assert second_res(DATA) == 2482
