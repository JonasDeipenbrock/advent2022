import math
from typing import List
from pprint import pprint
import numpy as np

reduce_worry = lambda x: math.floor(x / 3)


def read_monkey(monkey_input: List[str]):
    monkey = []
    monkey.append(
        [int(item) for item in monkey_input[1].replace(", ", " ").split()[2:]]
    )
    op = monkey_input[2].strip().split()

    def update_worry(worry: int):
        second_value = worry if op[5] == "old" else int(op[5])
        if op[4] == "+":
            return worry + second_value
        elif op[4] == "*":
            return worry * second_value

    monkey.append(update_worry)
    # monkey.append(f"def update(old): return {op}")
    divisor = monkey_input[3].strip().split()[3]
    target_true = monkey_input[4].strip().split()[5]
    target_false = monkey_input[5].strip().split()[5]

    def select_target(item: int):
        return int(target_true) if item % int(divisor) == 0 else int(target_false)

    monkey.append(select_target)
    monkey.append(int(divisor))
    return monkey


def get_input():
    with open("./input.txt", "r") as f:
        return f.readlines()


def solve_a(input: List[str]):
    monkeys = []
    monkeys_inspected = []
    for monkey_index in range(0, len(input), 7):
        monkey_input = input[monkey_index : monkey_index + 6]
        monkeys.append(read_monkey(monkey_input))
        monkeys_inspected.append(0)
    for round in range(1, 21):
        for idx, monkey in enumerate(monkeys):
            monkeys_inspected[idx] += len(monkey[0])
            for item in monkey[0]:
                monkey[0] = monkey[0][1:]
                increased_worry = monkey[1](item)
                decreased_worry = reduce_worry(increased_worry)
                target = monkey[2](decreased_worry)
                monkeys[target][0].append(decreased_worry)
                pprint(f"{round}: monkey {idx} throwing {item} to {target}")
    pprint(monkeys)
    monkeys_inspected.sort()
    pprint(monkeys_inspected)
    print(monkeys_inspected[-1] * monkeys_inspected[-2])


def solve_b(input: List[str]):
    monkeys = []
    monkeys_inspected = []
    mod_number = 1
    for monkey_index in range(0, len(input), 7):
        monkey_input = input[monkey_index : monkey_index + 6]
        monkey = read_monkey(monkey_input)
        monkeys.append(monkey)
        monkeys_inspected.append(0)
        mod_number *= monkey[3]
    # mod_number = np.prod([number for monkey in monkeys for number in monkey[0]])
    print(mod_number)
    # mod_number = int()
    super_reduce = lambda x: x % mod_number

    for round in range(1, 10001):
        for idx, monkey in enumerate(monkeys):
            monkeys_inspected[idx] += len(monkey[0])
            for item in monkey[0]:
                monkey[0] = monkey[0][1:]
                increased_worry = monkey[1](item)
                decreased_worry = super_reduce(increased_worry)
                target = monkey[2](decreased_worry)
                monkeys[target][0].append(decreased_worry)
                # pprint(f"{round}: monkey {idx} throwing {item} to {target}")
    # pprint(monkeys)
    monkeys_inspected.sort()
    pprint(monkeys_inspected)
    print(monkeys_inspected[-1] * monkeys_inspected[-2])
    pass


if __name__ == "__main__":
    input = get_input()
    solve_a(input)
    solve_b(input)
