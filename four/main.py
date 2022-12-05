import re


def get_input():
    with open("./input.txt", "r") as f:
        return f.readlines()


# 486
def solve_a(i):
    sum = 0
    for line in i:
        if find(line):
            sum += 1
    print(sum)


def find(line):
    one, two, three, four = re.split(",|-", line)
    one, two, three, four = int(one), int(two), int(three), int(four)
    return (one <= three and two >= four) or (one >= three and two <= four)


def solve_b(i):
    sum = 0
    for line in i:
        one, two, three, four = list(map(int, (re.split(",|-", line))))
        if (
            one >= three
            and one <= four
            or two >= three
            and two <= four
            or ((one <= three and two >= four) or (one >= three and two <= four))
        ):
            sum += 1
    print(sum)


if __name__ == "__main__":
    i = get_input()
    solve_a(i)
    solve_b(i)
