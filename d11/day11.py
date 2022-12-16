from d11.day11_input import DATA

test_input = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""


class Monkey:

    def __init__(self, number, items, operation, operation_value, test, test_true, test_false):
        self.number = number
        self.items = items
        self.test = test
        self.test_true = test_true
        self.test_false = test_false
        self.operation = operation
        self.operation_value = operation_value
        self.total = []

    def get_worry_level(self, value):
        value1 = self.operation_value if self.operation_value != 0 else value
        if self.operation == "+":
            return value + value1
        else:
            return value * value1

    def pass_to_monkey(self, monkeys, number, new_item):
        monkey = monkeys.get(number)
        monkey.items.append(new_item)

    def get_items(self):
        return self.items

    def get_total_count(self):
        return len(self.total)

    def process(self, denominator, monkeys, divide=False):
        for item in self.items:
            self.total.append(item)
            worry_level = self.get_worry_level(item)

            if divide:
                worry_level = int(worry_level / 3)

            if worry_level % self.test == 0:
                self.pass_to_monkey(monkeys, self.test_true, worry_level % denominator)
            else:
                self.pass_to_monkey(monkeys, self.test_false, worry_level % denominator)
        self.items = []


def read_data(data):
    monkeys_dict = dict()
    for monkey_data in data.split("\n\n"):
        number, items, operation, operation_value, test, test_true, test_false = 0, [], "", 0, 1, 0, 0
        for line in monkey_data.split("\n"):
            line = line.strip()
            if line.startswith("Monkey"):
                number = int(line.split(" ")[1].replace(":", "").strip())
            elif line.startswith("Starting items:"):
                items = [int(el) for el in line.replace("Starting items: ", "").split(", ")]
            elif line.startswith("Operation"):
                operation, operation_value = line.replace("Operation: new = old ", "").split(" ")
                operation_value = int(operation_value) if operation_value != 'old' else 0
            elif line.startswith("Test"):
                test = int(line.replace("Test: divisible by ", "").strip())
            elif line.startswith("If true:"):
                test_true = int(line.replace("If true: throw to monkey", "").strip())
            elif line.startswith("If false:"):
                test_false = int(line.replace("If false: throw to monkey", "").strip())
        monkey = Monkey(number, items, operation, operation_value, test, test_true, test_false)
        monkeys_dict[number] = monkey
    return monkeys_dict


def solution(data, rounds, divide):
    monkeys_dict = read_data(data)

    denominator = 1
    for monkey in monkeys_dict.values():
        denominator *= monkey.test

    for i in range(1, rounds + 1):
        for monkey in monkeys_dict.values():
            monkey.process(denominator, monkeys_dict, divide=divide)

    totals = sorted([monkey.get_total_count() for monkey in monkeys_dict.values()], reverse=True)
    return totals[0] * totals[1]


def first_res(data):
    return solution(data, 20,  True)


def second_res(data):
    return solution(data, 10000, False)


assert first_res(test_input) == 10605
assert first_res(DATA) == 113232

assert second_res(test_input) == 2713310158
assert second_res(DATA) == 29703395016
