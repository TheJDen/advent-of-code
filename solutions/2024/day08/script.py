from collections import *
from itertools import *
from functools import *
from string import *
from heapq import *
import time
import operator

def main():
    with open("input.txt") as f:
        grid = tuple(line.rstrip() for line in f)
    print(part1(grid))
    print(part2(grid))

def part1(grid):
    m, n = len(grid), len(grid[0])
    positions = defaultdict(list)
    for i in range(m):
        for j in range(n):
            if grid[i][j] == ".":
                continue
            positions[grid[i][j]].append((i, j))
    antinodes = set()
    for freq_positions in positions.values():
        for (x1, y1) in freq_positions:
            for (x2, y2) in freq_positions:
                if (x1, y1) == (x2, y2):
                    continue
                dx = x2 - x1
                dy = y2 - y1
                if 0 <= x2 + dx < m and 0 <= y2 + dy < n:
                    antinodes.add((x2 + dx, y2 + dy))
    return len(antinodes)
    
def part2(grid):
    m, n = len(grid), len(grid[0])
    positions = defaultdict(list)
    for i in range(m):
        for j in range(n):
            if grid[i][j] == ".":
                continue
            positions[grid[i][j]].append((i, j))
    antinodes = set()
    for freq_positions in positions.values():
        for (x1, y1) in freq_positions:
            for (x2, y2) in freq_positions:
                if (x1, y1) == (x2, y2):
                    continue
                dx = x2 - x1
                dy = y2 - y1
                antinodes.add((x2, y2))
                while 0 <= x2 + dx < m and 0 <= y2 + dy < n:
                    x2 += dx
                    y2 += dy
                    antinodes.add((x2, y2))
    return len(antinodes)

if __name__ == "__main__":
    main()
