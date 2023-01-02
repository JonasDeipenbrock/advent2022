from typing import List
from collections import defaultdict

UNPASSABLE = ["/", "\\", "_", "|", "*"]


def read_terrain(width: int, height: int):
    # terrain = defaultdict(lambda: " ")
    terrain = []
    # replace with/open and readline with input() for console input
    with open("franzi/example.txt", "r") as f:
        for i in range(height):
            # check if only valid tokens are in input here
            # it is enough to check that there is only valid items in here
            # so no need to check for each command
            line = f.readline()[:width]
            # for j in range(width):
            #     terrain[(i, j)] = line[j]
            terrain += line

    return terrain


def get_start_pos(terrain: List[str], width: int):
    try:
        if "X" not in terrain:
            rover_absolute = terrain.index("R")
            rover = rover_absolute // width, rover_absolute % width
            goal_absolute = terrain.index("x")
            goal = goal_absolute // width, goal_absolute % width
        else:
            absolute = terrain.index("X")
            rover = goal = absolute // width, absolute % width
    except:
        print("Error")
        return None, None
    return goal, rover


def debug(terrain: List[str], width: int, height: int):
    if not terrain:
        print("Error")
        return
    for i in range(height):
        line = ""
        for j in range(width):
            line += terrain[i * width + j]
        print(line, len(line))


def move(terrain, rover, direction: str, width: int, height: int, amount=1):
    for _ in range(amount):
        current = rover[0] * width + rover[1]
        next_field = get_next_field(width, current, direction)
        if terrain[next_field] in UNPASSABLE:
            break
        terrain[current] = " "
        if terrain[next_field] == "x":
            terrain[next_field] = "X"
        else:
            terrain[next_field] = "R"
        debug(terrain, width, height)
        rover = next_field // width, next_field % width
    return terrain, rover


def get_next_field(width, current, direction):
    # ! doesnt check if at border!
    match direction:
        case "up":
            return current - width
        case "down":
            return current + width
        case "left":
            return current - 1
        case "right":
            return current + 1


if __name__ == "__main__":
    terrain = None
    goal = rover = None
    while True:
        line = input()
        line = line.split(" ")
        match line[0]:
            case "new":
                width = int(line[1])
                height = int(line[2])
                # keine fehler behandlung bei fehlenden Werten (oder nicht ints)
                terrain = read_terrain(width, height)
                goal, rover = get_start_pos(terrain, width)
                print(goal, rover)
            case "up" | "down" | "left" | "right":
                if len(line) > 1:
                    terrain, rover = move(
                        terrain, rover, line[0], width, height, int(line[1])
                    )
                else:
                    terrain, rover = move(terrain, rover, line[0], width, height)
            case "debug":
                debug(terrain, width, height)
            case "path":
                pass
            case "debug-path":
                pass
            case "quit":
                exit(0)
