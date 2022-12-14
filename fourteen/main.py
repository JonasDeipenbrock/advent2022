from typing import List
from pprint import pprint
from collections import defaultdict


def get_input():
    with open("fourteen/input.txt", "r") as f:
        return f.readlines()


def solve_a(input: List[str]):
    path = [
        [pair.split(",", maxsplit=1) for pair in row.strip().split(" -> ")]
        for row in input
    ]
    path = [[(int(pair[0]), int(pair[1])) for pair in row] for row in path]
    start = (500, 0)
    blocked = defaultdict(lambda: 0)
    for row in path:
        if len(row) == 1:
            blocked[(row[0][0], row[0][1])] = 1
        for idx in range(len(row) - 1):
            pair1 = row[idx]
            pair2 = row[idx + 1]
            if pair1[0] == pair2[0]:
                x = pair1[0]
                y_range = range(min(pair1[1], pair2[1]), max(pair1[1], pair2[1]) + 1)
                for y in y_range:
                    blocked[(x, y)] = 1
            if pair1[1] == pair2[1]:
                y = pair1[1]
                x_range = range(min(pair1[0], pair2[0]), max(pair1[0], pair2[0]) + 1)  #
                for x in x_range:
                    blocked[(x, y)] = 1
    max_depth = max(pair[1] for row in path for pair in row)
    sand_pos = (500, 0)
    sand_number = 1
    while True:
        sx, sy = sand_pos
        if sy > max_depth:
            print(sand_number - 1)
            return sand_number
        if not (sx, sy + 1) in blocked:  # try below
            sand_pos = (sx, sy + 1)
        elif not (sx - 1, sy + 1) in blocked:  # try left below
            sand_pos = (sx - 1, sy + 1)
        elif not (sx + 1, sy + 1) in blocked:  # try right below
            sand_pos = (sx + 1, sy + 1)
        else:  # stop sand
            blocked[sand_pos] = 1
            sand_pos = (500, 0)
            sand_number += 1

    # create dict out of ranges of pairs
    # create range for pair
    # add entries of range to dict
    # for each position of falling sand test if there is an entry in the dict for next position
    #   if below lowest point of rock => return counter number
    #   if no entry fall down
    #   if entry sideways do that logic
    #   if stopped at sand current position to dict


def solve_b(input: List[str]):
    path = [
        [pair.split(",", maxsplit=1) for pair in row.strip().split(" -> ")]
        for row in input
    ]
    path = [[(int(pair[0]), int(pair[1])) for pair in row] for row in path]
    blocked = defaultdict(lambda: 0)
    for row in path:
        if len(row) == 1:
            blocked[(row[0][0], row[0][1])] = 1
        for idx in range(len(row) - 1):
            pair1 = row[idx]
            pair2 = row[idx + 1]
            if pair1[0] == pair2[0]:
                x = pair1[0]
                y_range = range(min(pair1[1], pair2[1]), max(pair1[1], pair2[1]) + 1)
                for y in y_range:
                    blocked[(x, y)] = 1
            if pair1[1] == pair2[1]:
                y = pair1[1]
                x_range = range(min(pair1[0], pair2[0]), max(pair1[0], pair2[0]) + 1)  #
                for x in x_range:
                    blocked[(x, y)] = 1
    max_depth = max(pair[1] for row in path for pair in row)

    # add floor
    for x in range(-10000, 10000):
        blocked[(x, max_depth + 2)] = 1

    sand_pos = (500, 0)
    sand_number = 1
    while True:
        sx, sy = sand_pos
        if (500, 0) in blocked:
            print(sand_number - 1)
            return sand_number
        if not (sx, sy + 1) in blocked:  # try below
            sand_pos = (sx, sy + 1)
        elif not (sx - 1, sy + 1) in blocked:  # try left below
            sand_pos = (sx - 1, sy + 1)
        elif not (sx + 1, sy + 1) in blocked:  # try right below
            sand_pos = (sx + 1, sy + 1)
        else:  # stop sand
            blocked[sand_pos] = 1
            sand_pos = (500, 0)
            sand_number += 1


if __name__ == "__main__":
    input = get_input()
    solve_a(input)
    solve_b(input)
