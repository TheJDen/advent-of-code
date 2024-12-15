from collections import *
from itertools import *
from functools import *
from string import *
from heapq import *
import time
import operator
import copy

def main():
    with open("input.txt") as f:
        grid = tuple(line.rstrip() for line in f)
    print(part1(grid))
    print(part2(grid))

def part1(grid):
    regions = defaultdict(list)
    m, n = len(grid), len(grid[0])
    def flood(i, j, letter, seen = None):
        seen = seen if seen is not None else set()
        if not 0 <= i < m or not 0 <= j < n or grid[i][j] != letter or (i, j) in seen:
            return seen
        seen.add((i, j))
        for di, dj in ((1,0), (0,1), (-1,0), (0, -1)):
            flood(i + di, j + dj, grid[i][j], seen)
        return seen
    visited = set()
    for i in range(m):
        for j in range(n):
            if (i, j) in visited:
                continue
            region = flood(i, j, grid[i][j])
            visited.update(region)
            regions[grid[i][j]].append(region)

    def price(letter, region):
        area = len(region)
        perimeter = 0
        for i, j in region:
            for di, dj in ((1,0), (0,1), (-1,0), (0, -1)):
                if not 0 <= i + di < m or not 0 <= j + dj < n or grid[i + di][j + dj] != letter:
                    perimeter += 1
        return area * perimeter
    return sum(sum(price(letter, region) for region in regions) for letter, regions in regions.items())

def part2(grid):
    regions = defaultdict(list)
    m, n = len(grid), len(grid[0])
    def flood(i, j, letter, seen = None):
        seen = seen if seen is not None else set()
        if not 0 <= i < m or not 0 <= j < n or grid[i][j] != letter or (i, j) in seen:
            return seen
        seen.add((i, j))
        for di, dj in ((1,0), (0,1), (-1,0), (0, -1)):
            flood(i + di, j + dj, grid[i][j], seen)
        return seen
    visited = set()
    for i in range(m):
        for j in range(n):
            if (i, j) in visited:
                continue
            region = flood(i, j, grid[i][j])
            visited.update(region)
            regions[grid[i][j]].append(region)
    ugh = [["*"] * (n + 2), *(["*", *line, "*"] for line in grid), ["*"] * (n + 2)]
    def price(letter, region):
        area = len(region)
        sides = 0
        visited = set()
        for i, j in sorted(region):
            if ugh[1 + i][j] == letter:
                continue
            start = (i + 1j * (j - 1))
            if start in visited:
                continue
            pos = start
            direction = 1
            while True:
                visited.add(pos)
                next_pos = pos + direction
                if (int(next_pos.real), int(next_pos.imag)) not in region:
                    pos = next_pos
                    visited.add(pos)
                    left = pos + direction * 1j
                    if (int(left.real), int(left.imag)) not in region:
                        direction *= 1j
                        pos += direction
                        sides += 1
                else:
                    direction *= -1j
                    sides += 1
                if pos == start and direction == 1:
                    break
        print(area, sides)
        return area * sides
    return sum(sum(price(letter, region) for region in regions) for letter, regions in regions.items())


if __name__ == "__main__":
    main()
