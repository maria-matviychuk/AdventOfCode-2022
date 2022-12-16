from d4.day4_input import DATA

test_input = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""


def first_res(data):
    res = 0
    pairs = data.split("\n")
    for p in pairs:
        s1, s2 = p.split(',')

        p11, p12 = s1.split('-')
        p21, p22 = s2.split('-')

        p11, p12 = int(p11), int(p12)
        p21, p22 = int(p21), int(p22)

        if p11 <= p21 and p12 >= p22:
            res += 1
        elif p11 >= p21 and p12 <= p22:
            res += 1

    return res


def second_res(data):
    res = 0
    pairs = data.split("\n")
    for p in pairs:
        s1, s2 = p.split(',')

        p11, p12 = s1.split('-')
        p21, p22 = s2.split('-')

        set_1 = set(range(int(p11), int(p12) + 1))
        set_2 = set(range(int(p21), int(p22) + 1))

        if set_1 & set_2:
            res += 1

    return res


assert first_res(test_input) == 2
assert first_res(DATA) == 503

assert second_res(test_input) == 4
assert second_res(DATA) == 827
