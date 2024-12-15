GALAXY = '#'
def part1(image, empty_distance = 2):
    empty_rows = {i for i, row in enumerate(image) if row.count(GALAXY) == 0}
    empty_cols = {j for j, col in enumerate(zip(*image)) if col.count(GALAXY) == 0}
    galaxies = [(i, j) for i, row in enumerate(image) for j, pos in enumerate(row) if pos == GALAXY]
    total = 0
    for galaxy1 in range(len(galaxies)):
        i1, j1 = galaxies[galaxy1]
        for galaxy2 in range(galaxy1 + 1, len(galaxies)):
            i2, j2 = galaxies[galaxy2]
            small_i, large_i = sorted([i1, i2])
            small_j, large_j = sorted([j1, j2])
            distance = 0
            for i in range(small_i, large_i):
                distance += 1 if i not in empty_rows else empty_distance
            for j in range(small_j, large_j):
                distance += 1 if j not in empty_cols else empty_distance
            total += distance
    return total


def part2(image):
    return part1(image, 1_000_000)


def main():
    with open("input.txt") as f:
        image = [line.rstrip() for line in f]
    print(part1(image))
    print(part2(image))


if __name__ == "__main__":
    main()