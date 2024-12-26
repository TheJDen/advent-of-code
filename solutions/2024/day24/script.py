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
    expressions = []
    with open("input.txt") as f:
        first, second = f.read().split("\n\n")
        for line in first.split("\n"):
            wire, val = line.split(": ")
            val_of[wire] = int(val)
        for line in second.rstrip().split("\n"):
            thing, end = line.split(" -> ")
            a, op, b = thing.split()
            expressions.append((a, op, b, end))
#    print(part1(val_of, expressions))
    print(part2(val_of, expressions))

def part1(val_of, expressions):
    get_from = {}
    for a, op, b, end in expressions:
        get_from[end] = (a, op, b)

    op_map = {
            "AND": operator.and_,
            "OR": operator.xor,
            "XOR": operator.xor,
            }

    def get_val(wire):
        if wire in val_of:
            return val_of[wire]
        a, op, b = get_from[wire]
        return op_map[op](get_val(a), get_val(b))

    wires = set(val_of) | {end for _, _, _, end in expressions}
    zwires = sorted(wire for wire in wires if wire.startswith("z"))
    zvals = [get_val(zwire) for zwire in zwires]
    return int("".join(str(zval) for zval in zvals)[::-1], 2)

def part2(val_of, expressions):
    input_wires = {}
    gate_with_output_wire = {}
    gate_op = {}
    for gate, (a, op, b, end) in enumerate(expressions):
        input_wires[gate] = a, b
        gate_with_output_wire[end] = gate
        gate_op[gate] = op
    op_map = {
            "AND": operator.and_,
            "OR": operator.xor,
            "XOR": operator.xor,
    }
    out_swaps = [("z18", "wss"), ("z08", "mvb"), ("z23", "bmn"), ("rds", "jss")]
    return ",".join(sorted(chain.from_iterable(out_swaps)))
    for a, b in out_swaps:
        gate1 = gate_with_output_wire[a]
        gate2 = gate_with_output_wire[b]
        gate_with_output_wire[a] = gate2
        gate_with_output_wire[b] = gate1

#    print("digraph {")
#    for output, gate in gate_with_output_wire.items():
#          a, b = input_wires[gate]
#          print(f"{a} -> {gate}")
#          print(f"{b} -> {gate}")
#          print(f"{gate} -> {output}")
#    print("}")
#    import sys
#    sys.exit()


    wires = set(val_of) | {end for _, _, _, end in expressions}
    xwires = sorted((wire for wire in wires if wire.startswith("x")), reverse=True)
    ywires = sorted((wire for wire in wires if wire.startswith("y")), reverse=True)
    zwires = sorted(wire for wire in wires if wire.startswith("z"))
    xvals = [val_of[xwire] for xwire in xwires]
    yvals = [val_of[ywire] for ywire in ywires]
    num1 = int("".join(map(str, xvals)), 2)
    num2 = int("".join(map(str, yvals)), 2)
    summ = num1 + num2
    summ_str = bin(summ)[2:][::-1]
    def get_val(wire, seen=None):
        seen = seen if seen is not None else set()
        if wire in seen:
            return None
        if wire in val_of:
            return val_of[wire]
        seen.add(wire)
        gate = gate_with_output_wire[wire]
        a, b = input_wires[gate]
        a_val = get_val(a, seen)
        if a_val is None:
            return None
        b_val = get_val(b, seen)
        if b_val is None:
            return None
        val = op_map[gate_op[gate]](a_val, b_val)
        seen.discard(wire)
        return val

    zvals = [get_val(zwire) for zwire in zwires]
    res_str = "".join(map(str, zvals))
    print(summ_str)
    print(res_str)
    for i, (b1, b2) in enumerate(zip(summ_str[::-1], res_str[::-1])):
        if b1 != b2:
            print(i)
    output_wires = tuple(gate_with_output_wire)
    candidates = []
    for i, a in enumerate(output_wires):
        for j in range(i + 1, len(output_wires)):
            b = output_wires[j]
            gate1 = gate_with_output_wire[a]
            gate2 = gate_with_output_wire[b]
            gate_with_output_wire[a] = gate2
            gate_with_output_wire[b] = gate1
            # check
            zvals = [get_val(zwire) for zwire in zwires]
            res_str = "".join(map(str, zvals))
            if res_str == summ_str:
                candidates.append((a,b))
            gate_with_output_wire[a] = gate1
            gate_with_output_wire[b] = gate2
    print(candidates)


if __name__ == "__main__":
    main()
