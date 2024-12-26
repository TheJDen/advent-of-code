from collections import *
from itertools import *
from functools import *
import re
from string import *
from heapq import *
import time
import operator
from math import *

def main():
    with open("input.txt") as f:
        grid = tuple(line.rstrip() for line in f)
    print(part1(grid))
    print(part2(grid))

def distance_from(grid, a):
    m, n = len(grid), len(grid[0])
    level = {a}
    d = {a: 0}
    for distance in count():
        if not level:
            return d
        next_level = set()
        for i, j in level:
            for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                if not 0 <= i + di < m  or not 0 <= j + dj < n:
                    continue
                if grid[i + di][j + dj] == "#" or (i + di, j + dj) in d:
                    continue
                d[(i + di, j + dj)] = distance + 1
                next_level.add((i + di, j + dj))
        level = next_level
    raise ValueError

def part1(grid):
    m, n = len(grid), len(grid[0])
    end = next((i, j) for i in range(m) for j in range(n) if grid[i][j] == "E")
    distance_from_end = distance_from(grid, end)
    total = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "#":
                continue
            for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                ni, nj = i + 2 * di, j + 2 * dj
                if not 0 <= ni < m  or not 0 <= nj < n:
                    continue
                if (ni, nj) not in distance_from_end:
                    continue
                save = distance_from_end[(i, j)] - (distance_from_end[(ni, nj)] + 2)
                if save < 0:
                    save = 0
                if save >= 100:
                    total += 1
    return total

def bfs(m, n, start, d, max_steps):
    level = {start}
    shortest_ending_at = {start: d[start]}
    for num_steps in range(1, max_steps + 1):
        next_level = set()
        for i, j in level:
            for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                if not 0 <= i + di < m or not 0 <= j + dj < n:
                    continue
                ni, nj = i + di, j + dj
                if (ni, nj) in shortest_ending_at:
                    continue
                shortest_ending_at[(ni, nj)] = num_steps + d.get((ni, nj), inf)
                next_level.add((ni, nj))
        level = next_level
    return shortest_ending_at

def part2(grid):
    m, n = len(grid), len(grid[0])
    end = next((i, j) for i in range(m) for j in range(n) if grid[i][j] == "E")
    distance_from_end = distance_from(grid, end)
    total = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "#":
                continue
            shortest_ending_at = bfs(m, n, (i, j), distance_from_end, 20)
            for _, shortest in shortest_ending_at.items():
                save = distance_from_end[(i, j)] - shortest
                if save >= 100:
                    total += 1
    return total

if __name__ == "__main__":
    main()
