from d2.day2_input import DATA

test_input = """
A Y
B X
C Z
"""


def first_res(data):
    res = 0
    lose, draw, win = 0, 3, 6
    rock, paper, scissors = 1, 2, 3
    rounds = data.strip().splitlines()
    
    for r in rounds:
        r1, r2 = r.split(' ')
        his = {'A': rock, 'B': paper, 'C': scissors}.get(r1)
        yours = {'X': rock, 'Y': paper, 'Z': scissors}.get(r2)

        res += yours
        if his == yours:
            res += draw
        if yours == rock and his == scissors:
            res += win
        if yours == paper and his == rock:
            res += win
        if yours == scissors and his == paper:
            res += win
    return res


def second_res(data):
    res = 0
    lose, draw, win = 0, 3, 6
    rock, paper, scissors = 1, 2, 3
    rounds = data.strip().splitlines()
    
    for r in rounds:
        r1, r2 = r.split(' ')
        his = {'A': rock, 'B': paper, 'C': scissors}.get(r1)
        yours = {'X': lose, 'Y': draw, 'Z': win}.get(r2)

        res += yours
        if yours == draw:
            res += his
        if yours == win and his == scissors:
            res += rock
        if yours == win and his == rock:
            res += paper
        if yours == win and his == paper:
            res += scissors
        if yours == lose and his == scissors:
            res += paper
        if yours == lose and his == rock:
            res += scissors
        if yours == lose and his == paper:
            res += rock

    return res


assert first_res(test_input) == 15
assert first_res(DATA) == 17189

assert second_res(test_input) == 12
assert second_res(DATA) == 13490
