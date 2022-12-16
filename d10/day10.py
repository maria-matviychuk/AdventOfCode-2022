from d10.day10_input import DATA

test_input = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""


def first_res(data):
    strength_signals = list(range(20, 221, 40))
    strengths = []
    cycle_number = 0
    total = 1

    def check():
        if cycle_number in strength_signals:
            strengths.append(cycle_number * total)

    for row in data.split("\n"):
        if row == "noop":
            cycle_number += 1
            check()
        else:
            cycle_number += 1
            check()
            cycle_number += 1
            check()
            value = int(row.split(" ")[1])
            total += value

    return sum(strengths)


def second_res(data):
    s = Solution()
    s.proceed(data)


class Solution:
    cycle_number = 0
    total = 1
    ctrt_row = 0
    pos_to_draw = 0
    x = 0

    def check(self, crt):
        self.cycle_number += 1
        if self.pos_to_draw in [self.x - 1, self.x, self.x + 1]:
            crt[self.ctrt_row][self.pos_to_draw] = '#'
        self.pos_to_draw += 1
        if self.cycle_number in list(range(40, 241, 40)):
            self.ctrt_row += 1
            self.pos_to_draw = 0

    def proceed(self, data):
        crt = []
        for i in range(20, 221, 40):
            tmp = []
            tmp[:40] = ['.'] * 40
            crt.append(tmp)

        for row in data.split("\n"):
            if row == "noop":
                self.check(crt)
            else:
                self.check(crt)
                self.check(crt)
                self.total += int(row.split(" ")[1])
                self.x = self.total

        for line in crt:
            print(line)


assert first_res(test_input) == 13140
assert first_res(DATA) == 11220

second_res(test_input)
# ##..##..##..##..##..##..##..##..##..##..
# ###...###...###...###...###...###...###.
# ####....####....####....####....####....
# #####.....#####.....#####.....#####.....
# ######......######......######......####
# #######.......#######.......#######.....

print('-'*40)
second_res(DATA)  # BZPAJELK
