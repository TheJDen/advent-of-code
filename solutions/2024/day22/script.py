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
    with open("input.txt") as f:
        nums = [int(line.rstrip()) for line in f]
    print(part1(nums))

import sys
sys.setrecursionlimit(3001)

def generate(num, num_processes=2000, seq=None):
    seq = seq if seq is not None else [num]
    if num_processes == 0:
        return seq
    num = num ^ (num * 64) % 16777216
    num = num ^ (num // 32) % 16777216
    num = num ^ (num * 2048) % 16777216
    seq.append(num)
    return generate(num, num_processes - 1, seq)

def sliding_window(iterable, n):
    "Collect data into overlapping fixed-length chunks or blocks."
    # sliding_window('ABCDEFG', 4) → ABCD BCDE CDEF DEFG
    iterator = iter(iterable)
    window = deque(islice(iterator, n - 1), maxlen=n)
    for x in iterator:
        window.append(x)
        yield tuple(window)

def part1(nums):
    seqs = [list(map(lambda x: x % 10, generate(num))) for num in nums]
    max_seen = [defaultdict(int) for seq in seqs]
    for i, seq in enumerate(seqs):
        for q in sliding_window(seq, 5):
            t = tuple(num2 - num1 for num1, num2 in pairwise(q))
            if t in max_seen[i]:
                continue
            max_seen[i][t] = max(max_seen[i][t], q[-1])
    print("cached")
    max_summ = 0
    for t in set(chain(*max_seen)):
        st = [max_seen[i][t] for i in range(len(seqs))]
        if sum(st) > max_summ:
            max_summ = sum(st)
    return max_summ


def part2(patterns, designs):
    patterns = set(patterns)
    @cache
    def num_ways(candidate) -> int:
        if not candidate:
            return 1
        total = 0
        for i in range(len(candidate)):
            left = candidate[:i + 1]
            if left not in patterns:
                continue
            right = candidate[i + 1:]
            total += num_ways(right)
        return total
    return sum(num_ways(design) for design in designs)

if __name__ == "__main__":
    main()
