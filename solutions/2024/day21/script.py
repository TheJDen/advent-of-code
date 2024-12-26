from collections import *
from itertools import *
from functools import *
import re
from string import *
from heapq import *
import time
import operator
from math import *

A = "A"
UP = "^"
DOWN = "v"
LEFT = "<"
RIGHT = ">"
directions = {
        UP: (1, 0),
        DOWN: (-1, 0),
        LEFT: (0, -1),
        RIGHT: (0, 1)
    }


NUM_PAD = (
    (None, "0", A),
    ("1", "2", "3"),
    ("4", "5", "6"),
    ("7", "8", "9")
)
DIR_PAD = (
    (LEFT, DOWN, RIGHT),
    (None, UP, A)
)
NUM_PAD_LOC = {button: (i, j) for i, row in enumerate(NUM_PAD) for j, button in enumerate(row) if button is not None}
DIR_PAD_LOC = {button: (i, j) for i, row in enumerate(DIR_PAD) for j, button in enumerate(row) if button is not None}

def main():
    with open("input.txt") as f:
        codes = f.read().rstrip().split('\n')
    print(part1(codes))
    print(part2(codes))

def possible_paths(pad_loc):
    possible = {}
    for button1, (i1, j1) in pad_loc.items():
        for button2, (i2, j2) in pad_loc.items():
            i_diff = i2 - i1
            j_diff = j2 - j1
            vert = DOWN if i_diff < 0 else UP
            horizontal = LEFT if j_diff < 0 else RIGHT
            candidates = set()
            if (i1, j2) in pad_loc.values():
                candidates.add(horizontal * abs(j_diff) + vert * abs(i_diff))
            if (i2, j1) in pad_loc.values():
                candidates.add(vert * abs(i_diff) + horizontal * abs(j_diff))
            possible[(button1, button2)] = list(candidates)
    return possible

POSSIBLE_PATHS_NUM = possible_paths(NUM_PAD_LOC)
POSSIBLE_PATHS_DIR = possible_paths(DIR_PAD_LOC)


def shortest_you_press(last_button, target_button, depth):
    candidates = POSSIBLE_PATHS_NUM[(last_button, target_button)]
    candidates = map(lambda s: s + A, candidates)
    for _ in range(depth):
        candidates = list(chain.from_iterable(map(shortest_one_level, candidates)))
    return min(candidates, key=len)

def shortest_one_level(s, i=0):
    if i == len(s):
        return [""]
    last = A if i == 0 else s[i - 1]
    all_possible = []
    for start in POSSIBLE_PATHS_DIR[(last, s[i])]:
        all_possible.extend([start + A + path for path in shortest_one_level(s, i + 1)])
    return all_possible
    

def part1(codes: list[str]):
    total = 0
    for code in codes:
        seq_parts = []
        for last_button, target_button in pairwise(A + code):
            seq_parts.append(shortest_you_press(last_button, target_button, depth=2))
        seq = "".join(seq_parts) 
        print(len(seq))
        num = int("".join(char for char in code if char.isdigit()))
        total += num * len(seq)
    return total

def dp_factory(depth):
    return partial(dp, depth=depth)

@cache
def dp(last_dir, dir, depth=25):
    if depth == 0:
        return 1
    paths = POSSIBLE_PATHS_DIR[(last_dir, dir)]
    return min(sum(starmap(dp_factory(depth-1), pairwise(A + path + A))) for path in paths)
        
def part2(codes: list[str]):
    total = 0
    for code in codes:
        seq_len = 0
        for last_button, target_button in pairwise(A + code):
            seqs = POSSIBLE_PATHS_NUM[(last_button, target_button)]
            seq_len += min(sum(starmap(dp_factory(25), pairwise(A + seq + A))) for seq in seqs)
        num = int("".join(char for char in code if char.isdigit()))
        total += num * seq_len
    return total
    



if __name__ == "__main__":
    main()
