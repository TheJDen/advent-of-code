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
    print(part2(stones))

def part1(stones):
    def get_num_stones(stone, remaining_blinks=25):
        if not remaining_blinks:
            return 1
        if stone == 0:
            return get_num_stones(1, remaining_blinks - 1)
        stone_str = str(stone)
        half, rem = divmod(len(stone_str), 2)
        if rem:
            return get_num_stones(stone * 2024, remaining_blinks - 1)
        left, right = stone_str[:half], stone_str[half:]
        num_left = get_num_stones(int(left), remaining_blinks - 1)
        num_right = get_num_stones(int(right), remaining_blinks - 1)
        return num_left + num_right
    return sum(get_num_stones(stone) for stone in stones)

def part2(stones):
    @cache
    def get_num_stones(stone, remaining_blinks=75):
        if not remaining_blinks:
            return 1
        if stone == 0:
            return get_num_stones(1, remaining_blinks - 1)
        stone_str = str(stone)
        half, rem = divmod(len(stone_str), 2)
        if rem:
            return get_num_stones(stone * 2024, remaining_blinks - 1)
        left, right = stone_str[:half], stone_str[half:]
        num_left = get_num_stones(int(left), remaining_blinks - 1)
        num_right = get_num_stones(int(right), remaining_blinks - 1)
        return num_left + num_right
    return sum(get_num_stones(stone) for stone in stones)

        
    
if __name__ == "__main__":
    main()
