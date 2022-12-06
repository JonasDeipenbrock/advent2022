from typing import List
import queue


def get_input():
    with open("./input.txt", "r") as f:
        return f.readlines()


def solve_a(input: List[str]):
    length = 4
    for line in input:
        find_marker(line, length)


def solve_b(input):
    length = 14
    for line in input:
        find_marker(line, length)


def find_marker(input: str, length: int):
    buffer = queue.Queue(length)
    for index, char in enumerate(input):
        if char in buffer.queue:
            buffer = clear_duplicate(buffer, char)
        buffer.put(char)
        if buffer.full():
            print(index + 1, char, buffer.queue)
            return


def clear_duplicate(buffer: queue.Queue, match_char: str):
    while not buffer.empty():
        char = buffer.get()
        if char == match_char:
            return buffer


if __name__ == "__main__":
    input = get_input()
    solve_a(input)
    solve_b(input)
