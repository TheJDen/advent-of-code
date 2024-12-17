from collections import *
from itertools import *
from functools import *
from math import inf
from re import A

from copy import *
from numpy import linalg
import numpy as np
from string import *
from heapq import *
import time
import operator
import matplotlib.pyplot as plt
import dataclasses

def main():
    with open("input.txt") as f:
        maze = tuple(line.rstrip() for line in f)
    print(part1(maze))
    print("p2")
    print(part2(maze))

@dataclasses.dataclass(order=True)
class MazeState:
    cost: int = dataclasses.field(compare=True)
    direction: complex = dataclasses.field(compare=False)
    path: list = dataclasses.field(compare=False)


def part1(maze):
    m, n = len(maze), len(maze[0])
    visited = set()
    start = next((i, j) for i in range(m) for j in range(n) if maze[i][j] == "S")
    end = next((i, j) for i in range(m) for j in range(n) if maze[i][j] == "E")
    min_heap = [MazeState(0, 1j, [start])]
    while min_heap:
        cost, direction, path = dataclasses.astuple(heappop(min_heap))
        if path[-1] == end:
            return cost
        visited.add((direction, path[-1]))
        turn_left = direction * 1j
        if (turn_left, path[-1]) not in visited:
            visited.add((turn_left, path[-1]))
            heappush(min_heap, MazeState(1000 + cost, turn_left, path))
        turn_right = direction * -1j
        if (turn_right, path[-1]) not in visited:
            visited.add((turn_right, path[-1]))
            heappush(min_heap, MazeState(1000 + cost, turn_right, path))
        di, dj = int(direction.real), int(direction.imag)
        i, j = path[-1]
        if 0 <= i + di < m and 0 <= j + dj < n and maze[i + di][j + dj] != "#" and (direction, i + di, j + dj) not in visited:
            visited.add((direction, i, j))
            heappush(min_heap, MazeState(1 + cost, direction, path + [(i + di, j + dj)]))
    return inf
            

def part2(maze):
    m, n = len(maze), len(maze[0])
    visited = {}
    start = next((i, j) for i in range(m) for j in range(n) if maze[i][j] == "S")
    end = next((i, j) for i in range(m) for j in range(n) if maze[i][j] == "E")
    min_heap = [MazeState(0, 1j, [start])]
    best_tiles = {start, end}
    best = None
    while min_heap:
        cost, direction, path = dataclasses.astuple(heappop(min_heap))
        if best is not None and cost > best:
            break
        if path[-1] == end and (best is None or cost == best):
            if best is None:
                best = cost
            best_tiles.update(path)
            continue
        if visited.get((direction, path[-1]), inf) < cost:
            continue
        visited[(direction, path[-1])] = cost
        turn_left = direction * 1j
        if visited.get((turn_left, path[-1]), 1000 + cost) >= 1000 + cost:
            visited[(turn_left, path[-1])] =  1000 + cost
            heappush(min_heap, MazeState(1000 + cost, turn_left, path))
        turn_right = direction * -1j
        if visited.get((turn_right, path[-1]), 1000 + cost) >= 1000 + cost:
            visited[(turn_right, path[-1])] =  1000 + cost
            heappush(min_heap, MazeState(1000 + cost, turn_right, path))
        di, dj = int(direction.real), int(direction.imag)
        i, j = path[-1]
        if 0 <= i + di < m and 0 <= j + dj < n and maze[i + di][j + dj] != "#" and visited.get((direction, i + di, j + dj), 1+ cost) >= 1 + cost:
            visited[(direction, (i + di, j + dj))] =  1 + cost
            heappush(min_heap, MazeState(1 + cost, direction, path + [(i + di, j + dj)]))
    return len(best_tiles)


if __name__ == "__main__":
    main()
