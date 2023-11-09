
from src import %day%

def load_puzzle_input(filename):
    puzzle_data = []

    with open(filename, "r") as filehandle:
        for line in filehandle:
            puzzle_data.append(line.strip())

    return puzzle_data

def part1():
    return %day%.part1()


def part2():
    return %day%.part2()


def part1_example():
    return %day%.part1_example()


def part2_example():
    return %day%.part2_example()
