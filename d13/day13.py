from d13.day13_input import DATA

test_input = """
[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
"""


def compare_lists(left, right):
    for i, value in enumerate(left):
        if i == len(right):
            return False
        res = compare(left[i], right[i])
        if isinstance(res, bool):
            return res

    if len(right) > len(left):
        return True


def compare(left, right):
    if isinstance(left, list) and isinstance(right, list):
        return compare_lists(left, right)
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return True
        if left > right:
            return False
    if isinstance(left, int) and isinstance(right, list):
        return compare([left], right)
    if isinstance(left, list) and isinstance(right, int):
        return compare(left, [right])


def first_res(data):
    inputs = []
    for line in data.strip().split("\n\n"):
        inputs.append([eval(l) for l in line.splitlines()])

    total = 0
    counter = 1
    for left, right in inputs:
        is_right_order = compare(left, right)
        if is_right_order:
            total = total + counter
        counter += 1

    return total


def sort_elements(data):
    for i in range(0, len(data) - 1):
        for j in range(0, len(data) - 1):
            if not compare(data[j], data[j + 1]):
                data[j], data[j + 1] = data[j + 1], data[j]
    return data


def second_res(data):
    divider1 = [[2]]
    divider2 = [[6]]

    inputs = []
    for line in data.strip().splitlines():
        if line.strip() == "":
            continue
        inputs.append(eval(line))

    inputs.append(divider1)
    inputs.append(divider2)
    new_input = sort_elements(inputs)

    return (new_input.index(divider1) + 1) * (new_input.index(divider2) + 1)


assert first_res(test_input) == 13
assert first_res(DATA) == 4894
assert second_res(test_input) == 140
assert second_res(DATA) == 24180
