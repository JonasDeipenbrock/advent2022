from typing import List
from pprint import pprint


def get_input():
    with open("./input.txt", "r") as f:
        return f.readlines()


def solve_a(input: List[str]):
    cycle = 0
    register = 1
    signal_strength = 0
    cycle_to_check = [20, 60, 100, 140, 180, 220]
    commands = [line.split() for line in input]
    queue = [
        (cmd, int(amount[0]) if amount != [] else None) for cmd, *amount in commands
    ]
    screen = ""
    sub_routine = False
    while queue != []:
        cycle += 1
        if (cycle - 1) % 40 - register in [-1, 0, 1]:
            screen += "#"
        else:
            screen += "."
        if cycle in cycle_to_check:
            signal_strength += cycle * register
        if queue[0][0] == "addx":
            if sub_routine:
                register += queue[0][1]
            sub_routine = not sub_routine
        # only flush command if not in sub_routine
        if not sub_routine:
            queue = queue[1:]
    print(signal_strength)
    print(screen[0:40])
    print(screen[40:80])
    print(screen[80:120])
    print(screen[120:160])
    print(screen[160:200])
    print(screen[200:240])
    pass


# def draw_pixel(screen: str, curr_position: int, sprite_position: int):
#     char = "."
#     if curr_position in range(sprite_position - 1, sprite_position + 2):
#         char = "#"
#         print(f"drawing at {curr_position}")
#     screen += char


def solve_b(input: List[str]):
    pass


if __name__ == "__main__":
    input = get_input()
    solve_a(input)
    solve_b(input)
