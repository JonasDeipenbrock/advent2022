from typing import List

""" 
X = 88 = Rock = 1
Y = 89 = Paper = 2
Z = 90 = Scissors = 3
=> -87 um 1 bis 3 zu bekommen

Rock - Rock = 0 => Draw
Rock + Rock = 2 => Draw
Rock - Paper = -1 => Paper win
Rock + Paper = 3 => Paper win
Rock - Scissor = -2 => Rock win
Rock + Scissor = 4 => Rock win
"""


def get_input():
    with open("./input.txt", "r") as f:
        return f.readlines()


def solve_a(i: List[str]):
    score = 0
    for line in i:
        theirs, mine = line.split(" ")
        theirs = ord(theirs.strip()) - 64
        mine = ord(mine.strip()) - 87
        score += mine
        if mine == theirs:
            score += 3
        elif (
            (mine == 1 and theirs == 3)
            or (mine == 2 and theirs == 1)
            or (mine == 3 and theirs == 2)
        ):
            score += 6
    print(score)


def solve_b(i):
    score = 0
    for line in i:
        theirs, mine = line.split(" ")
        theirs = ord(theirs.strip()) - 64
        mine = ord(mine.strip()) - 87

        if mine == 1:  # lose
            if theirs == 1:
                score += 3
            elif theirs == 2:
                score += 1
            else:
                score += 2
        elif mine == 2:  # draw
            score += 3
            score += theirs
        else:  # win
            score += 6
            if theirs == 1:
                score += 2
            elif theirs == 2:
                score += 3
            else:
                score += 1
    print(score)


if __name__ == "__main__":
    i = get_input()
    solve_a(i)
    solve_b(i)
