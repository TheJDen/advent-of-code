import string
DIGITS = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
    }

def part1(f):
    letter_stripped = (line.strip(string.ascii_letters + '\n') for line in f)
    return sum(int(line[0] + line[-1]) for line in letter_stripped)

def part2(f):
    return sum(10 * get_first_digit(line, range(len(line))) + get_first_digit(line, reversed(range(len(line)))) for line in f)

def get_first_digit(s, index_order):
    for i in index_order:
        if s[i] in string.digits:
            return int(s[i])
        for digit, num in DIGITS.items():
            if s[i: i + len(digit)] == digit:
                return num

def main():
    with open("input.txt") as f:
        #print(part1(f))
        print(part2(f))

if __name__ == "__main__":
    main()