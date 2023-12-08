from collections import Counter

FIVE_OF_A_KIND = 7
FOUR_OF_A_KIND = 6
FULL_HOUSE = 5
THREE_OF_A_KIND = 4
TWO_PAIR = 3
ONE_PAIR = 2
HIGH_CARD = 1

def get_hand_type_p1(hand):
    symbol_count_counts = Counter(Counter(hand).values())
    if symbol_count_counts[5] == 1:
        return FIVE_OF_A_KIND
    if symbol_count_counts[4] == 1:
        return FOUR_OF_A_KIND
    if symbol_count_counts[3] == 1 and symbol_count_counts[2] == 1:
        return FULL_HOUSE
    if symbol_count_counts[3] == 1:
        return THREE_OF_A_KIND
    if symbol_count_counts[2] == 2:
        return TWO_PAIR
    if symbol_count_counts[2] == 1:
        return ONE_PAIR
    return HIGH_CARD

def get_values(hand, val_str):
    return tuple(val_str[::-1].index(symbol) for symbol in hand)
        

def part1(hands, bids):
    return sum(rank * int(bids[i]) for rank, i in enumerate(sorted(range(len(hands)), key=lambda i: (get_hand_type_p1(hands[i]), get_values(hands[i], "AKQJT98765432"))), start=1))

def get_hand_type_p2(hand):
    return get_hand_type_p1(hand.replace('J', max("AKQT98765432", key=lambda char: hand.count(char))))
 

def part2(hands, bids):
    return sum(rank * int(bids[i]) for rank, i in enumerate(sorted(range(len(hands)), key=lambda i: (get_hand_type_p2(hands[i]), get_values(hands[i], "AKQT98765432J"))), start=1))


def parse_input(lines):
    hands = []
    bids = []
    for line in lines:
        hand, bid = line.split()
        hands.append(hand)
        bids.append(bid)
    return hands, bids

def main():
    with open("input.txt") as f:
        hands, bids = parse_input([line.rstrip() for line in f])
    print(part1(hands, bids))
    print(part2(hands, bids))


if __name__ == "__main__":
    main()