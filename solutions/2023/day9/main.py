import scipy
import numpy as np
from itertools import pairwise

def part1(histories):
    histories = [list(map(int, history)) for history in histories]
    total = 0
    for history in histories:
        diffs = [history]
        while any(diffs[-1]):
            diffs.append([num2 - num1 for num1, num2 in pairwise(diffs[-1])])
        for _ in range(1):
            diffs[-1].append(0)
            for next_diff, diff in pairwise(reversed(diffs)):
                diff.append(diff[-1] + next_diff[-1])
        total += diffs[0][-1]
    return total

def part2(histories):
    histories = [list(map(int, history)) for history in histories]
    total = 0
    for history in histories:
        diffs = [history]
        while any(diffs[-1]):
            diffs.append([num2 - num1 for num1, num2 in pairwise(diffs[-1])])
        extension = [[] for _ in range(len(diffs))]
        for _ in range(1):
            extension[-1].append(0)
            for i in reversed(range(len(diffs) - 1)):
                extension[i].append(diffs[i][0] - extension[i + 1][-1])
        total += extension[0][0]
    return total

def parse_input(lines):
    return [line.split() for line in lines]

def main():
    with open("input.txt") as f:
        histories = parse_input([line.rstrip() for line in f])
    print(part1(histories))
    print(part2(histories))


if __name__ == "__main__":
    main()