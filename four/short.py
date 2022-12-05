# fmt: off
import re
with open("./input.txt", "r") as f:
    contained, overlapped = 0, 0
    for line in f.readlines():
        one, two, three, four = list(map(int, (re.split(",|-", line))))
        if (one <= three and two >= four) or (one >= three and two <= four): contained += 1
        if (one <= four and three <= two): overlapped += 1
    print(contained, overlapped)

# remove re import by using something else
