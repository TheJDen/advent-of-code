def part1(times, distances):
    num_ways_can_beat = [sum((t - i) * i > d for i in range(1, t)) for t, d in zip(map(int, times), map(int, distances))]
    num_ways = 1
    for ways in num_ways_can_beat:
        if not ways:
            continue
        num_ways *= ways
    return num_ways

def part2(times, distances):
    race_time = int("".join(times))
    record_distance = int("".join(distances))
    return sum((race_time - i) * i > record_distance for i in range(1, race_time))

def parse_input(lines):
    times = lines[0].split(":")[1].strip().split()
    distances = lines[1].split(":")[1].strip().split()
    return times, distances

def main():
    with open("input.txt") as f:
        times, distances = parse_input([line.rstrip() for line in f])
    print(part1(times, distances))
    print(part2(times, distances))


if __name__ == "__main__":
    main()