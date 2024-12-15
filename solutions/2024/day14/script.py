from collections import *
from itertools import *
from functools import *
from math import inf

from numpy import linalg
import numpy as np
from string import *
from heapq import *
import time
import operator
import matplotlib.pyplot as plt

def main():
    robots = []
    with open("input.txt") as f:
        for line in f:
            p, v = line.rstrip().split()
            p = tuple(map(int, p[2:].split(",")))
            v = tuple(map(int, v[2:].split(",")))
            robots.append((p, v))
    print(part1(robots))

def part1(robots, X=101, Y=103):
    mx, my = X // 2, Y // 2
    quadrant_counts = [0] * 4
    grid = [[0] * X for _ in range(Y)]
    for (x, y), (dx, dy) in robots:
        fx, fy = (x + dx * 8270) % X, (y + dy * 8270) % Y
        grid[fy][fx] += 1
    for row in grid:
        print("".join("." if num == 0 else str(num) for num in row))

    x_var = []
    y_var = []
    v = []
    for i in range(8250,8300):
        xs = []
        ys = []

        for (x, y), (dx, dy) in robots:
            fx, fy = (x + dx * i) % X, (y + dy * i) % Y
            xs.append(fx)
            ys.append(fy)
            if fx == mx or fy == my:
                continue
            quadrant_counts[(fx < mx) * 2 + (fy < my)] += 1
        x_var.append(np.var(xs))
        y_var.append(np.var(ys))
        v.append(np.var(xs) + np.var(ys))
        

    plt.plot(v)
    plt.show()

    return reduce(operator.mul, quadrant_counts)
        
if __name__ == "__main__":
    main()
