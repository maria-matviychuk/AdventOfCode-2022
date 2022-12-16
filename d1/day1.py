from d1.day1_input import DATA

test_input = """
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""


def get_all_calories(data):
    calories = []
    for el in data.strip().split("\n\n"):
        res = sum([int(i) for i in el.split("\n")])
        calories.append(res)
    return calories


def first_res(data):
    return max(get_all_calories(data))


def second_res(data):
    return sum(sorted(get_all_calories(data))[-3:])


assert first_res(test_input) == 24000
assert first_res(DATA) == 69795

assert second_res(test_input) == 45000
assert second_res(DATA) == 208437
