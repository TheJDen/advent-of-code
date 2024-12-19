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
        a = int(next(f).rstrip().split()[-1])
        b = int(next(f).rstrip().split()[-1])
        c = int(next(f).rstrip().split()[-1])
        next(f)
        program = tuple(map(int, next(f).rstrip().split()[-1].split(",")))
    print(a, b, c, program)
    print(part1(a, b, c, program))
    print(part2(program))

@dataclasses.dataclass
class Register:
    a: int
    b: int
    c: int

class Machine:
    def combo(self, x) -> int:
        assert x != 7
        return x if x <= 3 else dataclasses.astuple(self.reg)[x - 4]

    def adv(self, x):
        self.reg.a >>= self.combo(x)

    def bxl(self, x):
        self.reg.b ^= x

    def bst(self, x):
        self.reg.b = self.combo(x) % 8

    def jnz(self, x):
        if self.reg.a == 0:
            return
        self.ip = x - 2

    def bxc(self, x):
        self.reg.b ^= self.reg.c

    def out(self, x):
        self.outputs.append(self.combo(x) % 8)

    def bdv(self, x):
        self.reg.b = self.reg.a >> self.combo(x)

    def cdv(self, x):
        self.reg.c = self.reg.a >> self.combo(x)

    def run_program(self, program, reg: Register):
        self.reg = reg
        self.ip = 0
        self.outputs = []
        instruction = {
            0: self.adv,
            1: self.bxl,
            2: self.bst,
            3: self.jnz,
            4: self.bxc,
            5: self.out,
            6: self.bdv,
            7: self.cdv
        }
        while self.ip < len(program) - 1:
            opcode = program[self.ip]
            operand = program[self.ip + 1]
            instruction[opcode](operand)
            self.ip += 2
        return tuple(self.outputs)


def part1(a, b, c, program):
    reg = Register(a, b, c)
    output = Machine().run_program(program, reg)
    return ",".join(map(str, output))

def part2(program):
    candidates = [0]
    for start in reversed(range(len(program))):
        suffix = program[start:]
        new_candidates = []
        for candidate in candidates:
            for i in range(8):
                if tuple(get_seq(8 * candidate + i)) == suffix:
                    new_candidates.append(8 * candidate + i)
        candidates = new_candidates
    return candidates






def get_seq(x):
    seq  = []
    while x:
        seq.append((x ^ (x >> ((x % 8) ^ 7))) % 8)
        x //= 8
    return seq
    
if __name__ == "__main__":
    main()
