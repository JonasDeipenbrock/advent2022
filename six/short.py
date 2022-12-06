# fmt: off
with open("./input.txt", "r") as f:
    line = f.readline()
    def find(length):
        substr = [line[i : i + length] for i in range(len(line))]
        return [idx + length for idx, hit in enumerate(substr) if isUnique(hit)][0]
    def isUnique(str):
        return len(list(set(str))) == len(list(str))
    print(find(4), find(14))
