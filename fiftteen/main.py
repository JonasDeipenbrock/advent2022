from typing import List
import re
from pprint import pprint
from collections import defaultdict


def get_input():
    with open("fiftteen/input.txt", "r") as f:
        return f.readlines()


def man_dist(x, y, sx, sy):
    return abs(x - sx) + abs(y - sy)


def solve_a(input: List[str]):
    points = []
    all_things = set()
    positions = [[int(c) for c in re.findall("-?\d+", line)] for line in input]
    for (x, y, sx, sy) in positions:
        distance = man_dist(x, y, sx, sy)
        points.append((x, y, distance))
        all_things.add((x, y))
        all_things.add((sx, sy))
    minimum_x_point = min(points, key=lambda x: x[0] - x[2])
    maximum_x_point = max(points, key=lambda x: x[0] + x[2])
    min_x = minimum_x_point[0] - minimum_x_point[2]
    max_x = maximum_x_point[0] + maximum_x_point[2]
    y = 10
    on_line = set()

    for x in range(min_x, max_x + 1):
        for sx, sy, ds in points:
            if (x, y) in all_things:
                continue
            if man_dist(x, y, sx, sy) <= ds:
                on_line.add((x, y))
    pprint(len(on_line))


def solve_b(input: List[str]):
    positions = [[int(c) for c in re.findall("-?\d+", line)] for line in input]
    radius = {(x, y): man_dist(x, y, sx, sy) for (x, y, sx, sy) in positions}
    scanners = radius.keys()

    acofs, bcofs = [], []
    for ((x, y), r) in radius.items():
        acofs.append(y - x + r + 1)
        acofs.append(y - x - r - 1)
        bcofs.append(x + y + r + 1)
        bcofs.append(x + y - r - 1)
    acofs = {a for a in acofs if acofs.count(a) >= 2}
    bcofs = {b for b in bcofs if bcofs.count(b) >= 2}

    xy = 4000000
    for a in acofs:
        for b in bcofs:
            p = ((b - a) // 2, (a + b) // 2)
            if all(0 < c < xy for c in p):
                if all(
                    man_dist(p[0], p[1], tx, ty) > radius[(tx, ty)]
                    for tx, ty in scanners
                ):
                    print(xy * p[0] + p[1], p[0], p[1])


if __name__ == "__main__":
    input = get_input()
    solve_a(input)
    solve_b(input)
