import string

NOT_SYMBOL = string.digits + '.'
ADJ = ((1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1))

def part(lines, i, j):
    start = end = j
    while start > 0 and lines[i][start - 1] in string.digits:
        start -= 1
    while end < len(lines[i]) and lines[i][end] in string.digits:
        end += 1
    return (i, start, end)

def get_unique_parts(lines, is_symbol: callable):
    parts = []
    for i, row in enumerate(lines):
        for j, char in enumerate(row):
            close_parts = set()
            if not is_symbol(char):
                continue
            for di, dj in ADJ:
                if not 0 <= i + di < len(row):
                    continue
                if not 0 <= j + dj < len(row):
                    continue
                if lines[i + di][j + dj] not in string.digits:
                    continue
                close_parts.add(part(lines, i + di, j + dj))
            parts.append(close_parts)
    return [[lines[i][start: end] for i, start, end in part] for part in parts]
    

def get_gear_parts(lines, is_symbol: callable):
    gears = []
    for i, row in enumerate(lines):
        for j, char in enumerate(row):
            close_parts = set()
            if not is_symbol(char):
                continue
            for di, dj in ADJ:
                if not 0 <= i + di < len(row):
                    continue
                if not 0 <= j + dj < len(row):
                    continue
                if lines[i + di][j + dj] not in string.digits:
                    continue
                close_parts.add(part(lines, i + di, j + dj))
            if len(close_parts) == 2:
                    gears.append(close_parts)
    return [[lines[i][start: end] for i, start, end in parts] for parts in gears]
    
def part1(parts):
    return sum(int(part_num_str) for part in parts for part_num_str in part)

def part2(gears):
    return sum(int(part1) * int(part2) for part1, part2 in gears)


def main():
    with open("input.txt") as f:
        lines = [line.rstrip() for line in f]
    print(part1(get_unique_parts(lines, lambda char: char not in NOT_SYMBOL)))
    print(part2(get_gear_parts(lines, lambda char: char == '*')))

if __name__ == "__main__":
    main()