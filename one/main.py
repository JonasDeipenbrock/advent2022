def get_input():
    with open("./input.txt", "r") as f:
        return f.readlines()


def solve_a(i):
    c_sum = 0
    c_index = 0
    max_sum = 0
    max_index = 0
    for line in i:
        if line == "\n":
            if max_sum < c_sum:
                max_sum = c_sum
                max_index = c_index
            c_sum = 0
            c_index += 1
        else:
            c_sum += int(line)
    print(max_sum, max_index)


def solve_b(i):
    sums = []
    c_sum = 0
    for line in i:
        if line == "\n":
            sums.append(c_sum)
            c_sum = 0
        else:
            c_sum += int(line)
    sums.sort(reverse=True)
    max_three = sums[0] + sums[1] + sums[2]
    print(max_three)


if __name__ == "__main__":
    i = get_input()
    solve_a(i)
    solve_b(i)
