from sympy import Eq, solveset, symbols, sympify

from d21.day21_input import DATA

test_input = """
root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32
"""


def read_data(data):
    d = dict()
    for line in data.strip().splitlines():
        name, operation = line.split(': ')
        d[name] = dict()
        if operation.strip().isnumeric():
            d[name]["number"] = int(operation)
        else:
            m1, op, m2 = operation.strip().split(' ')
            d[name]["wait"] = [m1, m2]
            d[name]["op"] = op
    return d


def get_monkey_number(monkeys, name):
    m = monkeys.get(name)
    if 'number' in m:
        return m["number"]
    name1, name2 = m['wait']
    number1 = get_monkey_number(monkeys, name1)
    number2 = get_monkey_number(monkeys, name2)
    op = m["op"]
    return eval(f"{number1}{op}{number2}")


def first_res(data):
    monkeys = read_data(data)
    res = get_monkey_number(monkeys, 'root')
    return res


def get_monkey_number2(monkeys, name):
    m = monkeys.get(name)
    if name == 'humn':
        return 'x'

    if 'number' in m:
        return m["number"]
    name1, name2 = m['wait']
    number1 = get_monkey_number2(monkeys, name1)
    number2 = get_monkey_number2(monkeys, name2)
    op = m["op"]
    return f"({number1}{op}{number2})"


def second_res(data):
    monkeys = read_data(data)
    monkeys['root']['op'] = '='

    root = monkeys['root']
    name1, name2 = root['wait']
    res1 = get_monkey_number2(monkeys, name1)
    res2 = get_monkey_number2(monkeys, name2)
    if 'x' in res1:
        equality = eval(res2)
        s = res1
    else:
        equality = eval(res1)
        s = res2

    expr = sympify(s)
    x = symbols('x')
    res = solveset(Eq(expr, equality), x)
    return int(res.args[0])


assert first_res(test_input) == 152
assert first_res(DATA) == 38731621732448

assert second_res(test_input) == 301
assert second_res(DATA) == 3848301405790
