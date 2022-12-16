from collections import defaultdict

from d5.day5_input import DATA

test_input = """
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""


def solution(data, is_reverse=True):
    matrix = []
    movements = []
    numbers = None

    c = defaultdict(list)

    for l in data.split("\n"):
        if len(l) < 1:
            continue
        if l.strip().startswith('['):
            matrix.append(l)
        elif l.strip().startswith('move'):
            movements.append(l)
        else:
            numbers = l

    matrix_len = len(numbers.split('   '))

    for m in matrix:
        m = list(m)
        for i in range(matrix_len):
            el = m[i*4 + 1]
            if el.strip() != "":
                c[i].append(el)

    for m in movements:
        tmp = m.split(' ')
        amount, from_, to_ = int(tmp[1]), int(tmp[3]), int(tmp[5])
        move(c, amount, from_, to_, is_reverse=is_reverse)

    res = ""
    for i in sorted(c.keys()):
        res += c[i][0]

    print(res)
    return res


def move(c, amount, from_, to_, is_reverse=False):
    to_move = c[from_-1][:amount]
    c[from_-1] = c[from_-1][amount:]
    if is_reverse:
        to_move.reverse()
    c[to_-1] = to_move + c[to_-1]


def first_res(data):
    return solution(data)


def second_res(data):
    return solution(data, is_reverse=False)


assert first_res(test_input) == "CMZ"
assert first_res(DATA) == "WCZTHTMPS"

assert second_res(test_input) == "MCD"
assert second_res(DATA) == "BLSGJSDTS"
