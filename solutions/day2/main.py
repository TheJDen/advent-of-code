from collections import Counter
from itertools import accumulate
RED = 12
GREEN = 13
BLUE = 14

def part1(rounds):
    for round in rounds:
        counts = Counter()
        for count_str, color in round:
            counts[color] += int(count_str)
        if counts["red"] > RED or counts["green"] > GREEN or counts["blue"] > BLUE:
            return False
    return True
        

def part2(rounds):
    reds = list(accumulate((int(count_str) for round in rounds for count_str, color in round if color == "red"), max))
    greens = list(accumulate((int(count_str) for round in rounds for count_str, color in round if color == "green"), max))
    blues = list(accumulate((int(count_str) for round in rounds for count_str, color in round if color == "blue"), max))
    return reds[-1] * greens[-1] * blues[-1]

def main():
    total = 0
    with open("input.txt") as f:
        for line in f:
            id_num_str, rest = line.split(':')
            #id_num = int(id_num_str[5:].strip())
            rounds = [[t.split() for t in round.split(', ')] for round in rest.strip().split(';')]
            # if part1(rounds):
            #     total += id_num
            total += part2(rounds)
        print(total)
        
if __name__ == "__main__":
    main()