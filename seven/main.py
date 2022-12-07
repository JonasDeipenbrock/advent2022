from typing import List

File = (str, int)
Dir = (str, int, [File])


class File:
    name: str
    size: int

    def __init__(self, name, size) -> None:
        self.name = name
        self.size = size

    def __str__(self) -> str:
        return self.name


class Dir:
    name: str
    size: int
    parent: Dir
    files = []
    dirs = []

    def __init__(self, name, parent) -> None:
        self.name = name
        self.parent = parent

    def add_file(self, file):
        self.files.append(file)

    def add_dir(self, dir):
        self.dirs.append(dir)

    def find_dir(self, name):
        print(f"looking for {name} in {self.name}")
        if self.name == name:
            return self
        for dir in self.dirs:
            if dir.find_dir(name):
                return dir
        return None

    def get_size(self):
        for dir in self.dirs:
            self.size += dir.get_size()
        for file in self.files:
            self.size += file.size
        return self.size

    # def __str__(self) -> str:
    #     string_arr = [self.name]
    #     for file in self.files:
    #         string_arr.append(file.__str__())
    #     for dir in self.dirs:
    #         string_arr.append(dir.__str__())
    #     return self.name


def get_input():
    with open("./seven/example.txt", "r") as f:
        return f.readlines()


def solve_a(input):
    root = read_input(input)


def solve_b(input):
    pass


def read_input(input: List[str]) -> Dir:
    root_dir = Dir("/", None)
    curr_dir = root_dir
    for line in input:
        front, back, *args = line.strip().split()
        if front != "$":
            if front == "dir":
                dir = Dir(back, curr_dir)
                print(back, curr_dir.name)
                curr_dir.add_dir(dir)
            else:
                file = File(back, front)
                print(back, curr_dir.name)
                curr_dir.add_file(file)
        elif front == "$":
            if back == "cd":
                if args[0] == "..":
                    curr_dir = curr_dir.parent
                else:
                    curr_dir = root_dir.find_dir(args[0])
                print("switching to", curr_dir.name)


if __name__ == "__main__":
    input = get_input()
    solve_a(input)
    solve_b(input)
