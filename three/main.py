def get_input():
    with open("./input.txt", "r") as f:
        return f.readlines()


def solve_a(i):
    prio = 0
    for line in i:
        length = int(len(line) / 2)
        first: str = line[:length]
        second: str = line[(length):]
        prio += find_common(first, second)
    print(prio)


def find_common(first, second, third=[]):
    for char in first:
        if char in second:
            if third and not char in third:
                continue
            offset = 96
            if not char.islower():
                offset = 64 - 26
            return ord(char) - offset


def solve_b(i):
    prio = 0
    for index in range(0, len(i), 3):
        one, two, three = i[index : index + 3]
        prio += find_common(one, two, three)
    print(prio)


if __name__ == "__main__":
    i = get_input()
    solve_a(i)
    solve_b(i)
