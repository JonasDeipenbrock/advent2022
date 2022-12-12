from typing import List
from pprint import pprint
import math
from collections import defaultdict


def get_input():
    with open("./input.txt", "r") as f:
        return f.readlines()


def create_grid(input: List[str]):
    grid = [list(row.strip()) for row in input]
    n = len(grid)
    m = len(grid[0])

    # save start and target
    sx, sy = [(x, y) for x in range(n) for y in range(m) if grid[x][y] == "S"][0]
    ex, ey = [(x, y) for x in range(n) for y in range(m) if grid[x][y] == "E"][0]

    # reset start and target
    grid[sx][sy] = "a"
    grid[ex][ey] = "z"

    # transform grid to have numbers
    grid = [[ord(height) - ord("a") for height in row] for row in grid]
    return grid, n, m, sx, sy, ex, ey


def find_path(grid, queue, ex, ey, n, m):
    distance = defaultdict(lambda: 1000000)
    # set distance for start to zero
    for x, y in queue:
        distance[(x, y)] = 0

    while len(queue) != 0:
        # take next from queue
        x, y = queue[0]
        queue = queue[1:]

        # print answer if at goal
        if (x, y) == (ex, ey):
            print(distance[(x, y)])

        # update neighbours
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            neighbour_x, neighbour_y = x + dx, dy + y

            #! make sure neighbour is on grid
            if neighbour_x in range(n) and neighbour_y in range(m):
                # check if distance is shorter than current
                if grid[x][y] >= grid[neighbour_x][neighbour_y] - 1:
                    new_distance = distance[x, y] + 1
                    if new_distance < distance[neighbour_x, neighbour_y]:
                        queue.append((neighbour_x, neighbour_y))
                        distance[neighbour_x, neighbour_y] = new_distance


def solve_a(input: List[str]):
    grid, n, m, sx, sy, ex, ey = create_grid(input)

    # only take S position as start
    queue = [(sx, sy)]

    find_path(grid, queue, ex, ey, n, m)


def solve_b(input: List[str]):
    grid, n, m, _, _, ex, ey = create_grid(input)

    # find other starting positions
    queue = [(x, y) for x in range(n) for y in range(m) if grid[x][y] == 0]

    find_path(grid, queue, ex, ey, n, m)


if __name__ == "__main__":
    input = get_input()
    solve_a(input)
    solve_b(input)
