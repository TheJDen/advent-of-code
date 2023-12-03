from itertools import accumulate
from collections import Counter, defaultdict

import string

NOT_SYMBOL = string.digits + '.'
ADJ = ((1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1))

def part(lines, i, j):
    start = end = j
    while start > 0 and lines[i][start - 1] in string.digits:
        start -= 1
    while end < len(lines[i]) and lines[i][end] in string.digits:
        end += 1
    return (i, start, end)

def process_input(lines):
    #parts = set()
    gears = []
    for i, row in enumerate(lines):
        for j, char in enumerate(row):
            close_parts = set()
            #if char in NOT_SYMBOL:
            if char != '*':
                continue
            for di, dj in ADJ:
                if not 0 <= i + di < len(row):
                    continue
                if not 0 <= j + dj < len(row):
                    continue
                if lines[i + di][j + dj] not in string.digits:
                    continue
                close_parts.add(part(lines, i + di, j + dj))
            if len(close_parts) == 2:
                    gears.append(close_parts)
            #parts.update(close_parts)
    return [[lines[i][start: end] for i, start, end in parts] for parts in gears]
    

def part1(part_num_strs):
    return sum(int(part_num_str) for part_num_str in part_num_strs)

def part2(gears):
    return sum(int(part1) * int(part2) for part1, part2 in gears)


def main():
    with open("input.txt") as f:
        inputs = process_input([line.rstrip() for line in f])
        print(inputs)
    #print(part1(inputs))
    print(part2(inputs))

if __name__ == "__main__":
    main()