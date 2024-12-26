from collections import *
from itertools import *
from functools import *
from string import *
from heapq import *
import time
import operator

def main():
    with open("input.txt") as f:
        grid = tuple(tuple(map(int, line.rstrip())) for line in f)
    print(part1(grid))
    print(part2(grid))

def part1(grid):
    m, n = len(grid), len(grid[0])
    @cache
    def backtrack(i, j, num=0):
        if not 0 <= i < m or not 0 <= j < m or grid[i][j] != num:
            return set()
        if grid[i][j] == 9:
            return {(i, j)}
        end = set()
        for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            end.update(backtrack(i + di, j + dj, num + 1))
        return end
    return sum(len(backtrack(i, j)) for i in range(m) for j in range(n))

def part2(grid):
    m, n = len(grid), len(grid[0])
    @cache
    def backtrack(i, j, num=0):
        if not 0 <= i < m or not 0 <= j < m or grid[i][j] != num:
            return 0
        if grid[i][j] == 9:
            return 1
        end = 0
        for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            end += backtrack(i + di, j + dj, num + 1)
        return end
    return sum(backtrack(i, j) for i in range(m) for j in range(n))

if __name__ == "__main__":
    main()
