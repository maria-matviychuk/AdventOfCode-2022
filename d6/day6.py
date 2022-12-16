from d6.day6_input import DATA

test_input = """zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"""


def solution(data, prefix_size=4):
    data = list(data)
    unique = data[:prefix_size]

    for i in range(prefix_size, len(data)):
        if len(set(unique)) < prefix_size:
            unique = unique[1:]
            unique.append(data[i])
        else:
            return i
    return len(data)


def first_res(data):
    return solution(data)


def second_res(data):
    return solution(data, prefix_size=14)


assert first_res("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 7
assert first_res("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5
assert first_res("nppdvjthqldpwncqszvftbrmjlhg") == 6
assert first_res("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10
assert first_res("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 11
assert first_res(DATA) == 1140

assert second_res("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 19
assert second_res("bvwbjplbgvbhsrlpgdmjqwftvncz") == 23
assert second_res("nppdvjthqldpwncqszvftbrmjlhg") == 23
assert second_res("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 29
assert second_res("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 26
assert second_res(DATA) == 3495
