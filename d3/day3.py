from string import ascii_lowercase, ascii_uppercase
from day3_input import DATA

test_input = """
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""


def get_intersections(data):
    intersections = []
    rucksacks = data.strip().splitlines()
    for r in rucksacks:
        full_len = len(r)
        if full_len < 2:
            continue
        r = list(r)
        first_r = set(r[:int(full_len/2)])
        second_r = set(r[int(full_len/2):])
        intersections.append(first_r.intersection(second_r).pop())
    return intersections


def sum_priorities(data):
    def count_priority(letter):
        if letter.isupper():
            return ascii_uppercase.find(letter) + 27
        else:
            return ascii_lowercase.find(letter) + 1

    # print(data)
    return sum(map(count_priority, data))


def first_res(data):
    return sum_priorities(get_intersections(data))


def get_intersections_by_3(data):
    intersections = []
    rucksacks = data.strip().splitlines()
    for i in range(0, len(rucksacks) - 2, 3):
        first = rucksacks[i]
        second = rucksacks[i + 1]
        third = rucksacks[i + 2]
        intersections.append((set(first) & set(second) & set(third)).pop())
    return intersections


def second_res(data):
    return sum_priorities(get_intersections_by_3(data))


assert first_res(test_input) == 157
assert first_res(DATA) == 8072

assert second_res(test_input) == 70
assert second_res(DATA) == 2567
