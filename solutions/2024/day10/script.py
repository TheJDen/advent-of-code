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

def part1(grid):
    m, n = len(grid), len(grid[0])
    def score(i, j, num=0):
        if not 0 <= i < m or not 0 <= j < n or grid[i][j] != num:
            return set()
        if num == 9:
            return {(i, j)}
        total = set()
        for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            total.update(score(i + di, j + dj, num + 1))
        return total
    return sum(len(score(i, j)) for i in range(m) for j in range(n))
    
if __name__ == "__main__":
    main()
