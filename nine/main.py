from typing import List
from pprint import pprint


def get_input():
    with open("./input.txt", "r") as f:
        return f.readlines()


def follow(head: tuple, tail: tuple):
    """Calculates the tails position to follow the head"""
    x, y = head[0] - tail[0], head[1] - tail[1]
    abs_x, abs_y = abs(x), abs(y)
    if abs_x > 1 or abs_y > 1:  # follow head
        return (
            tail[0] + (0 if x == 0 else x // abs_x),
            tail[1] + (0 if y == 0 else y // abs_y),
        )
    return tail


def solve_a(input: List[str]):
    # starting position? => start with 100 by 100 grid and start in middle somewhere
    # solve movement based on input => move head
    # move tail so it matches rules and add each visited position to dict {(x, y)}
    # take size of dict for final answer
    dirs = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}
    commands = [row.split() for row in input]
    moves = [(dirs[cmd], int(steps)) for cmd, steps in commands]
    knots = 10
    rope = [(0, 0) for _ in range(knots)]  # gives head and tail
    visited = [{rope[x]} for x in range(knots)]
    for direction, steps in moves:
        for _ in range(steps):
            head = rope[0]
            rope[0] = head[0] + direction[0], head[1] + direction[1]
            for i in range(1, knots):
                rope[i] = follow(rope[i - 1], rope[i])
                visited[i].add(rope[i])
    print(len(visited[1]))  # add one to this for some reason for correct answer
    print(len(visited[9]))

    pass


def solve_b(input):
    pass


if __name__ == "__main__":
    input = get_input()
    solve_a(input)
    solve_b(input)
