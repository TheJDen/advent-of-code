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
        stones = tuple(map(int, f.read().rstrip().split()))
    print(part1(stones))

def part1(stones):
    @cache
    def num_stones(stone, remaining_blinks=75):
        if not remaining_blinks:
            return 1
        if stone == 0:
            return num_stones(1, remaining_blinks - 1)
        stone_str = str(stone)
        half, rem = divmod(len(stone_str), 2)
        if rem == 1:
            return num_stones(stone * 2024, remaining_blinks - 1)
        left, right = int(stone_str[:half]), int(stone_str[half:])
        return num_stones(left, remaining_blinks - 1) + num_stones(right, remaining_blinks - 1)
    return sum(num_stones(s) for s in stones)
    
if __name__ == "__main__":
    main()
