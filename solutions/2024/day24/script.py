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
    val_of = {}
    idk = []
    with open("input.txt") as f:
        first, second = f.read().split("\n\n")
        for line in first.split("\n"):
            wire, val = line.split(": ")
            val_of[wire] = int(val)
        for line in second.rstrip().split("\n"):
            thing, end = line.split(" -> ")
            a, op, b = thing.split()
            idk.append((a, op, b, end))
    print(part1(val_of, idk))
    print(part2(val_of, idk))

def part1(val_of, idk):
    get_from = {}
    for a, op, b, end in idk:
        get_from[end] = (a, op, b)

    op_map = {
            "AND": operator.and_,
            "OR": operator.or_,
            "XOR": operator.xor,
            }

    def get_val(wire):
        if wire in val_of:
            return val_of[wire]
        a, op, b = get_from[wire]
        return op_map[op](get_val(a), get_val(b))

    wires = set(val_of) | {end for _, _, _, end in idk}
    zwires = sorted(wire for wire in wires if wire.startswith("z"))
    zvals = [get_val(zwire) for zwire in zwires]
    print(zvals)
    return int("".join(str(zval) for zval in zvals)[::-1], 2)

def part2(val_of, idk):
    get_from = {}
    for a, op, b, end in idk:
        get_from[end] = (a, op, b)

    op_map = {
            "AND": operator.and_,
            "OR": operator.or_,
            "XOR": operator.xor,
            }

    num1 = int("".join(str(v) for w, v in val_of.items() if w.startswith("x"))[::-1], 2)
    num2 = int("".join(str(v) for w, v in val_of.items() if w.startswith("y"))[::-1], 2)
    w = list(map(int, bin(num1 + num2)[2:]))

    def get_val(wire):
        if wire in val_of:
            return val_of[wire]
        a, op, b = get_from[wire]
        return op_map[op](get_val(a), get_val(b))

    wires = set(val_of) | {end for _, _, _, end in idk}
    zwires = sorted(wire for wire in wires if wire.startswith("z"))
    zvals = [get_val(zwire) for zwire in zwires]
    print(zvals)
    r = int("".join(str(zval) for zval in zvals)[::-1], 2)
    weird = [i for i in range(len(zvals)) if zvals[i] != w[i]]
    print(",".join(sorted(zwires[i] for i in weird)))






if __name__ == "__main__":
    main()
