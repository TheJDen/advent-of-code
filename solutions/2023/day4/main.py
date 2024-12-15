import math  
def part1(cards):
    return sum(math.floor(2 ** (sum(want_num in have_nums for want_num in want_nums) - 1))  for want_nums, have_nums in cards)
   
from functools import cache

def part2(cards):
    @cache
    def total_cards(i=0):
        if i >= len(cards):
            return 0
        want_nums, have_nums = cards[i]
        num_matching = sum(want_num in have_nums for want_num in want_nums)
        total = 1 + sum(total_cards(i + j) for j in range(1, num_matching + 1))
        return total

    return sum(total_cards(i) for i in range(len(cards)))

def part2_bottom_up(cards):
    total_cards = [0] * len(cards)
    for i in reversed(range(len(cards))):
        want_nums, have_nums = cards[i]
        num_matching = sum(want_num in have_nums for want_num in want_nums)
        total_cards[i] = 1 + sum(total_cards[i + j] for j in range(1, num_matching + 1))
    return sum(total_cards)

def main():
    with open("input.txt") as f:
        cards = []
        for line in f:
            title, remaining_card = line.rstrip().split(':')
            cards.append([section.strip().split() for section in remaining_card.rstrip().split('|')] )
    #print(part1(cards))
    #print(part2(cards))
    print(part2_bottom_up(cards))


if __name__ == "__main__":
    main()