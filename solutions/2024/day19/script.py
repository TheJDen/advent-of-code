from collections import *
from itertools import *
from functools import *
import re
from string import *
from heapq import *
import time
import operator

def main():
    with open("input.txt") as f:
        pattern_text, designs_text = f.read().rstrip().split("\n\n")
        patterns = pattern_text.split(", ")
        designs = designs_text.split("\n")
    print(part1(patterns, designs))
    print(part2(patterns, designs))

def part1(patterns, designs):
    patterns = set(patterns)
    @cache
    def is_possible(candidate) -> bool:
        if not candidate:
            return True
        for i in range(len(candidate)):
            left = candidate[:i + 1]
            if left not in patterns:
                continue
            right = candidate[i + 1:]
            if is_possible(right):
                return True
        return False
    return sum(is_possible(design) for design in designs)

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
