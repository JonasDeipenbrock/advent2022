from typing import List
import re


def get_input():
    with open("./input.txt", "r") as f:
        return f.readlines()


def solve_a(i: List[str]):
    delim = i.index("\n")
    stack_input = i[:delim]
    raw_commands = i[delim + 1 :]
    stack = load_stacks(stack_input)
    commands = load_commands(raw_commands)
    FINAL_STACK = apply_commands(stack, commands)
    extract_answer(FINAL_STACK)


def extract_answer(FINAL_STACK: List[List[str]]):
    answer = ""
    for sub_stack in FINAL_STACK:
        answer += sub_stack.pop()
    print(answer)


def apply_commands_multi_pop(stack: List[List[str]], commands: List[List[int]]):
    for command in commands:
        amount, source, target = command
        source -= 1
        target -= 1
        sub = []
        for _ in range(1, amount + 1):
            element = stack[source].pop()
            sub.append(element)
        sub.reverse()
        stack[target] += sub
    return stack


def apply_commands(stack: List[List[str]], commands: List[List[int]]):
    for command in commands:
        amount, source, target = command
        source -= 1
        target -= 1
        for _ in range(1, amount + 1):
            element = stack[source].pop()
            stack[target].append(element)
    return stack


def load_commands(cm):
    final_commands = []
    for command in cm:
        matches = re.findall("\d+", command)
        final_commands.append(list(map(int, matches)))
    return final_commands


def load_stacks(input: List[str]):
    stack = []
    input.reverse()
    for index, char in enumerate(input[0]):
        if char.isnumeric():
            sub_stack = []
            for idx in range(1, len(input)):
                token = input[idx][index]
                if not token == " ":
                    sub_stack.append(input[idx][index])
            stack.append(sub_stack)

    return stack


def solve_b(i):
    delim = i.index("\n")
    stack_input = i[:delim]
    raw_commands = i[delim + 1 :]
    stack = load_stacks(stack_input)
    commands = load_commands(raw_commands)
    FINAL_STACK = apply_commands_multi_pop(stack, commands)
    extract_answer(FINAL_STACK)


if __name__ == "__main__":
    i = get_input()
    solve_a(i.copy())
    solve_b(i.copy())
