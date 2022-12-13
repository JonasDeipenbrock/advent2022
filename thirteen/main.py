from typing import List
import ast
from pprint import pprint
from functools import cmp_to_key


def get_input():
    with open("thirteen/input.txt", "r") as f:
        return f.readlines()


def compare(left, right):
    # both are int
    if isinstance(left, int) and isinstance(right, int):
        return (left > right) - (
            left < right
        )  # if equal => return false should check rest of list
    # both are list
    elif isinstance(left, list) and isinstance(right, list):
        for comparision in map(compare, left, right):
            if comparision:
                return comparision
        return compare(len(left), len(right))
    else:
        if isinstance(left, list):
            right = [right]
        else:
            left = [left]
        return compare(left, right)


def solve_a(input: List[str]):
    pairs = [
        (ast.literal_eval(input[i].strip()), ast.literal_eval(input[i + 1].strip()))
        for i in range(0, len(input), 3)
    ]
    result = 0
    for idx, (left, right) in enumerate(pairs):
        if compare(left, right) == -1:
            result += idx + 1
    print(result)


def solve_b(input: List[str]):
    lines = [ast.literal_eval(row.strip()) for row in input if row != "\n"]
    lines.append([[2]])
    lines.append([[6]])
    lines.sort(key=cmp_to_key(compare))
    idx_a = lines.index([[2]]) + 1
    idx_b = lines.index([[6]]) + 1
    print(idx_a * idx_b)
    pass


if __name__ == "__main__":
    input = get_input()
    solve_a(input)
    solve_b(input)
