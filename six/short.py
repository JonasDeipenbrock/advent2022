# fmt: off
with open("./input.txt", "r") as f:
    line = f.readline()
    def find(length):
        print([idx + length for idx, hit in enumerate([line[i : i + length] for i in range(len(line))]) if len(list(set(hit))) == len(list(hit))][0])
    find(4), find(14)
