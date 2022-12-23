from copy import copy

from d20.day20_input import DATA

test_input = """
1
2
-3
3
-2
0
4
"""


def read_data(data):
    return [int(el) for el in data.strip().splitlines()]


def get_element(ordered, position):
    shift = position % len(ordered)
    pos_0 = ordered.index(0)
    new_index = (pos_0 + shift) % len(ordered)
    return ordered[new_index]


def first_res(data):
    original = read_data(data)
    reordered = copy(original)
    stable = copy(original)
    for item in original:
        if item == 0:
            continue

        current_index = stable.index(item)
        assert reordered[current_index] == item

        reordered.pop(current_index)
        stable.pop(current_index)

        new_index = current_index + item
        new_index = new_index % len(stable)

        if new_index < 0:
            new_index = len(stable) + new_index

        if new_index == 0 and item < 0:
            reordered.append(item)
            stable.append(0)
        else:
            reordered.insert(new_index, item)
            stable.insert(new_index, 0)

    return get_element(reordered, 1000) + get_element(reordered, 2000) + get_element(reordered, 3000)


def mix_items(original, stable, reordered):
    for item in original:
        if item == 0:
            continue

        current_index = stable.index(item)
        reordered.pop(current_index)
        stable.pop(current_index)

        new_index = current_index + item
        new_index = new_index % len(stable)

        if new_index < 0:
            new_index = len(stable) + new_index

        if new_index == 0 and item < 0:
            reordered.append(item)
            stable.append(0)
        else:
            reordered.insert(new_index, item)
            stable.insert(new_index, 0)


def mix_items_universal(original, positional):
    length = len(positional)
    for i in range(length):
        value = original[i]
        if value == 0:
            continue

        current_index = positional.index(i)
        positional.pop(current_index)

        new_index = current_index + value
        new_index = new_index % len(positional)

        if new_index < 0:
            new_index = len(positional) + new_index

        if new_index == 0 and i < 0:
            positional.append(i)
        else:
            positional.insert(new_index, i)


def get_el(original, ordered, position):
    shift = position % len(ordered)
    pos_0 = original.index(0)
    pos_0_positional = ordered.index(pos_0)
    positional_index = (pos_0_positional + shift) % len(ordered)
    positional_value = ordered[positional_index]
    return original[positional_value]


def second_res(data):
    initial = read_data(data)

    original = []
    for el in initial:
        original.append(el * 811589153)

    positional = list(range(len(original)))

    for i in range(0, 10):
        mix_items_universal(original, positional)

    num = get_el(original, positional, 1000)
    num2 = get_el(original, positional, 2000)
    num3 = get_el(original, positional, 3000)
    return num + num2 + num3


assert first_res(test_input) == 3
assert first_res(DATA) == 5962

assert second_res(test_input) == 1623178306
assert second_res(DATA) == 9862431387256