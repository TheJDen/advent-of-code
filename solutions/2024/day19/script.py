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
        pattern_text, design_text = f.read().split("\n\n")
        patterns = set(pattern_text.rstrip().split(", "))
        designs = design_text.rstrip().split("\n")
    print(part1(patterns, designs))
    print(part2(patterns, designs))

def part1(patterns, designs):
    @cache
    def is_possible(candidate):
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
    @cache
    def num_ways(candidate):
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
