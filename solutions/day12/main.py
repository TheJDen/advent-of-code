OPERATIONAL = '.'
DAMAGED = '#'
UNKNOWN = '?'
from functools import cache

@cache
def num_ways(springs, damaged, i=0, j=0, num_damaged=0):
    if i == len(springs):
        return j == len(damaged)
    num_ways_operational = lambda: num_ways(springs, damaged, i + 1, j + (num_damaged > 0)) if num_damaged == 0 or j < len(damaged) and num_damaged == damaged[j] else 0
    num_ways_damaged = lambda: num_ways(springs, damaged, i + 1, j, num_damaged + 1) if j < len(damaged) and num_damaged < damaged[j] else 0
    spring = springs[i]
    if spring == OPERATIONAL:
        return num_ways_operational()
    if spring == DAMAGED:
        return num_ways_damaged()
    return num_ways_operational() + num_ways_damaged()

def part1(row_springs, row_damaged):
    total = 0
    for springs, damaged in zip(row_springs, row_damaged):
        easier_springs = springs + OPERATIONAL
        damaged_nums = tuple(map(int, damaged))
        total += num_ways(easier_springs, damaged_nums)
    return total

def part2(row_springs, row_damaged):
    total = 0
    for springs, damaged in zip(row_springs, row_damaged):
        unfolded_springs = '?'.join((springs,) * 5) + OPERATIONAL
        unfolded_damaged_nums = tuple(map(int, damaged)) * 5
        total += num_ways(unfolded_springs, unfolded_damaged_nums)
    return total


def parse_input(lines):
    row_springs = []
    row_damaged = []
    for line in lines:
        springs, damaged_list_str = line.split()
        row_springs.append(springs)
        row_damaged.append(damaged_list_str.split(','))
    return row_springs, row_damaged

def main():
    with open("input.txt") as f:
        row_springs, row_damaged = parse_input([line.rstrip() for line in f])
    print(part1(row_springs, row_damaged))
    print(part2(row_springs, row_damaged))


if __name__ == "__main__":
    main()