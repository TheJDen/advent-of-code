from collections import *
from itertools import *
from functools import *
import re
from string import *
from heapq import *
import time
import operator

def main():
    with open("input.txt") as f:
        byte_positions = tuple(tuple(map(int, line.rstrip().split(","))) for line in f)
    print(part1(byte_positions))
    print(part2(byte_positions))

def part1(byte_positions):
    n = 71
    blocked = [[False] * n for _ in range(n)]
    for _, (x, y) in zip(range(1024), byte_positions):
        blocked[x][y] = True
    start = (0, 0)
    end = (n - 1, n - 1)
    level = {start}
    visited = {start}
    for num_steps in count():
        print(len(level))
        if end in level:
            return num_steps
        next_level = set()
        for i, j in level:
            for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                if not 0 <= i + di < n or not 0 <= j + dj < n:
                    continue
                if blocked[i + di][j + dj] or (i + di, j + dj) in visited:
                    continue
                visited.add((i + di, j + dj))
                next_level.add((i + di, j + dj))
        level = next_level

def part1(byte_positions):
    n = 71
    blocked = [[False] * n for _ in range(n)]
    for (x, y) in byte_positions:
        blocked[x][y] = True
        start = (0, 0)
        end = (n - 1, n - 1)
        level = {start}
        visited = {start}
        for _ in count():
            if end in level:
                break
            if not level:
                return x, y
            next_level = set()
            for i, j in level:
                for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                    if not 0 <= i + di < n or not 0 <= j + dj < n:
                        continue
                    if blocked[i + di][j + dj] or (i + di, j + dj) in visited:
                        continue
                    visited.add((i + di, j + dj))
                    next_level.add((i + di, j + dj))
            level = next_level

def part2(stones):
    pass
    
if __name__ == "__main__":
    main()
