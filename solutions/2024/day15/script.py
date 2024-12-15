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

def main():
    with open("input.txt") as f:
        warehouse_text, movements_text = f.read().rstrip().split("\n\n")
        warehouse = list(map(list, warehouse_text.split("\n")))
        movements = movements_text.split("\n")
    print(part1(deepcopy(warehouse), movements))
    print(part2(warehouse, movements))

def part1(warehouse, movements):
    m, n = len(warehouse), len(warehouse[0])
    d = {">": (0, 1), "^":(-1, 0), "<": (0, -1), "v": (1, 0)}
    i, j = next((i, j) for i in range(m) for j in range(n) if warehouse[i][j] == "@")
    for movement_list in movements:
        for move in movement_list:
            di, dj = d[move]
            for num_steps in count(1):
                ni, nj = i + di * num_steps, j + dj * num_steps
                if not 0 <= ni < m or not 0 <= nj < n or warehouse[ni][nj] == "#":
                    break
                if warehouse[ni][nj] == ".":
                    warehouse[i][j] = "."
                    warehouse[i + di][j + dj] = "@"
                    if num_steps > 1:
                        warehouse[ni][nj] = "O"
                    i, j = i + di, j + dj
                    break
    summ = 0
    for i in range(m):
        for j in range(n):
            if warehouse[i][j] != "O":
                continue
            summ += 100 * i + j
    return summ


                    
def part2(warehouse, movements):
    double = {".": "..", "#": "##", "@": "@.", "O": "[]"}
    new_warehouse = [list(chain.from_iterable(map(double.get, row))) for row in warehouse]

    def can_move_vert(i, j, di):
        if new_warehouse[i][j] == "#":
            return False
        if new_warehouse[i][j] == ".":
            return True
        if new_warehouse[i][j] == "[":
            return can_move_vert(i + di, j, di) and can_move_vert(i + di, j + 1, di)
        elif new_warehouse[i][j] == "]":
            return can_move_vert(i + di, j, di) and can_move_vert(i + di, j - 1, di)
        return can_move_vert(i + di, j, di)

    def can_move_horizontal(i, j, dj):
        for num_steps in count(1):
            if new_warehouse[i][j + num_steps * dj] == "#":
                return False
            if new_warehouse[i][j + num_steps * dj] == ".":
                return True

    def can_move(i, j, di, dj):
        return can_move_vert(i, j, di) if di in (-1, 1) else can_move_horizontal(i, j, dj)

    def move_vert(i, j, di):
        if new_warehouse[i][j] == "#":
            raise ValueError
        if new_warehouse[i][j] == ".":
            return
        if new_warehouse[i][j] == "[":
            move_vert(i + di, j, di)
            move_vert(i + di, j + 1, di)
            new_warehouse[i + di][j:j + 2], new_warehouse[i][j:j + 2] = new_warehouse[i][j:j + 2], new_warehouse[i + di][j:j + 2]
        elif new_warehouse[i][j] == "]":
            move_vert(i + di, j - 1, di)
            move_vert(i + di, j, di)
            new_warehouse[i + di][j - 1:j + 1], new_warehouse[i][j - 1:j + 1] = new_warehouse[i][j - 1:j + 1], new_warehouse[i + di][j - 1:j + 1]
        else:
            move_vert(i + di, j, di)
            new_warehouse[i + di][j], new_warehouse[i][j] = new_warehouse[i][j], new_warehouse[i + di][j]

    def move_horizontal(i, j, dj):
        if new_warehouse[i][j] == ".":
            return
        move_horizontal(i, j + dj, dj)
        new_warehouse[i][j], new_warehouse[i][j + dj] = new_warehouse[i][j + dj], new_warehouse[i][j] 

    def move(i, j, di, dj):
        if di in (-1, 1):
            move_vert(i, j, di)
        else:
            move_horizontal(i, j, dj)

    m, n = len(new_warehouse), len(new_warehouse[0])
    d = {">": (0, 1), "^":(-1, 0), "<": (0, -1), "v": (1, 0)}
    i, j = next((i, j) for i in range(m) for j in range(n) if new_warehouse[i][j] == "@")
    for movement_list in movements:
        for di, dj in map(d.get, movement_list):
            if can_move(i, j, di, dj):
                move(i, j, di, dj)
                i += di
                j += dj
    summ = 0
    for i in range(m):
        for j in range(n):
            if new_warehouse[i][j] != "[":
                continue
            summ += 100 * i + j
    return summ

if __name__ == "__main__":
    main()
