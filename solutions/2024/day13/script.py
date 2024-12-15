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

def main():
    machines = []
    with open("input.txt") as f:
        for machine in f.read().rstrip().split("\n\n"):
            a_spec, b_spec, prize_spec = machine.split("\n")
            ax_spec, ay_spec = a_spec.split(": ")[1].split(", ")
            bx_spec, by_spec = b_spec.split(": ")[1].split(", ")
            px_spec, py_spec = prize_spec.split(": ")[1].split(", ")
            ax, ay = int(ax_spec[2:]), int(ay_spec[2:])
            bx, by = int(bx_spec[2:]), int(by_spec[2:])
            px, py = int(px_spec[2:]), int(py_spec[2:])
            machines.append(((ax, ay), (bx, by), (px, py)))
    print(part1(machines))
    print(part2(machines))

def get_min_cost(ax, ay, bx, by, px, py, a_cost, b_cost):
    den = ax * by - ay * bx
    if den == 0:
        return inf
    x = (px * by - py * bx) / den
    if not x.is_integer():
        return inf
    y = (ax * py - ay * px) / den
    if not y.is_integer():
        return inf
    num_a, num_b =(x),(y)
    return num_a * a_cost + num_b * b_cost

def part1(machines, a_cost=3, b_cost=1):
    fewest_tokens = 0
    for (ax, ay), (bx, by), (px, py) in machines:
        tokens = get_min_cost(ax, ay, bx, by, px, py, a_cost, b_cost)
        if tokens == inf:
            continue
        fewest_tokens += tokens
    return fewest_tokens
        
def part2(machines, a_cost=3, b_cost=1):
    fewest_tokens = 0
    for (ax, ay), (bx, by), (px, py) in machines:
        tokens = get_min_cost(ax, ay, bx, by, px + 10000000000000, py + 10000000000000, a_cost, b_cost)
        if tokens == inf:
            continue
        fewest_tokens += tokens
    return fewest_tokens
    
if __name__ == "__main__":
    main()
