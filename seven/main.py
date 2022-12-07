from typing import List
from collections import defaultdict


def get_input():
    with open("./input.txt", "r") as f:
        return f.readlines()


def solve_a(input: List[str]):
    dir = defaultdict(int)
    root = []
    for line in input:
        match line.split():
            # current dir done, move to next in line
            case ["$", "cd", ".."]:
                root.pop()
            # add dir to processing
            case ["$", "cd", d]:
                root.append(d)
            # ignore ls commands
            case ["$", "ls"]:
                pass
            # ignore reads from ls => get handles via `cd a`
            case ["dir", d]:
                pass
            # sum files
            case [size, file]:
                # add file size to index
                dir[tuple(root)] += int(size)
                # take all parent paths
                path = root[:-1]
                # for each parent path add file size to their size
                while path:
                    dir[tuple(path)] += int(size)
                    path.pop()

    # filter all dirs with value <= 100000 and sum them
    small_dirs = [d for d in dir.values() if d <= 100000]
    sum_dirs = sum(small_dirs)
    print(sum_dirs)

    # calculate needed space
    available_space = 70000000 - dir[("/",)]
    needed_space = 30000000
    possible_dirs = [d for d in dir.values() if d + available_space >= needed_space]
    best_dir = min(possible_dirs)
    print(best_dir)


def solve_b(input):
    pass


if __name__ == "__main__":
    input = get_input()
    solve_a(input)
    solve_b(input)
