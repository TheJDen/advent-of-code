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
    locks = []
    keys = []
    with open("input.txt") as f:
        schematics = f.read().rstrip().split("\n\n")
        for s in schematics:
            scheme = s.split("\n")
            if scheme[0].count("#") == 0:
                keys.append(scheme)
            else:
                locks.append(scheme)
    print(part1(locks,keys))


def part1(locks, keys):
    lock_heights = [[sum(c == "#" for c in col) - 1 for col in zip(*lock)] for lock in locks]
    key_heights = [[sum(c == "#" for c in col) - 1 for col in zip(*key)] for key in keys]
    print(lock_heights)
    print(key_heights)
    return sum(all(hl + hk <= 5 for hl, hk in zip(l, k)) for l in lock_heights for k in key_heights)


if __name__ == "__main__":
    main()
