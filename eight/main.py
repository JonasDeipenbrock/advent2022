from typing import List


def get_input():
    with open("./input.txt", "r") as f:
        return f.readlines()


def solve_a(input: List[str]):
    grid = convert_input(input)
    visible = set()

    for x in range(len(input[0].strip())):
        max_tree = -1
        for y in range(len(input)):
            if grid[(x, y)] > max_tree:
                visible.add((x, y))
                max_tree = grid[(x, y)]
        # inverse
        max_tree = -1
        for y in reversed(range(len(input))):
            if grid[(x, y)] > max_tree:
                visible.add((x, y))
                max_tree = grid[(x, y)]
    for y in range(len(input)):
        max_tree = -1
        for x in range(len(input[0].strip())):
            if grid[(x, y)] > max_tree:
                visible.add((x, y))
                max_tree = grid[(x, y)]
        # reversed
        max_tree = -1
        for x in reversed(range(len(input[0].strip()))):
            if grid[(x, y)] > max_tree:
                visible.add((x, y))
                max_tree = grid[(x, y)]
    print(len(visible))

    scores = [
        scenic_score(x, y, input, grid)
        for y, row in enumerate(input)
        for x, tree in enumerate(row.strip())
    ]
    print(max(scores))


def scenic_score(x, y, input: List[str], grid):
    right, left, up, down = 0, 0, 0, 0
    for i in range(x + 1, len(input[0].strip())):
        if grid[(i, y)] < grid[(x, y)]:
            right += 1
        else:
            right += 1
            break
    for i in range(x - 1, -1, -1):
        if grid[(i, y)] < grid[(x, y)]:
            left += 1
        else:
            left += 1
            break
    for i in range(y + 1, len(input)):
        if grid[(x, i)] < grid[(x, y)]:
            down += 1
        else:
            down += 1
            break
    for i in range(y - 1, -1, -1):
        if grid[(x, i)] < grid[(x, y)]:
            up += 1
        else:
            up += 1
            break
    return up * down * left * right


def convert_input(input: List[str]):
    grid = {
        (x, y): int(tree)
        for y, row in enumerate(input)
        for x, tree in enumerate(row.strip())
    }
    return grid


def solve_b(input):
    pass


if __name__ == "__main__":
    input = get_input()
    solve_a(input)
    solve_b(input)
