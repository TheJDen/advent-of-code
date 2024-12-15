def part1(seeds, mappings):

    def mapped_vals(mapping):
        last_vals = seeds if mapping == 0 else mapped_vals(mapping - 1)
        new_vals = []
        for val in last_vals:
            for destination, source, length in mappings[mapping]:
                if source <= val < source + length:
                    new_vals.append(destination + val - source)
                    break
            else:
                new_vals.append(val)
        return new_vals
        
    return min(mapped_vals(len(mappings) - 1))


def get_seed_ranges(seeds):
    return [(seeds[i], seeds[i + 1]) for i in range(0, len(seeds) - 1, 2)]

def part2(seeds, mappings):
    
    seed_ranges = set(get_seed_ranges(seeds))

    def map_ranges(mapping):
        unmapped_ranges = seed_ranges if mapping == 0 else map_ranges(mapping - 1)
        mapped_ranges = set()
        for destination, source, map_range_length in mappings[mapping]:
            mapped = set()
            unmapped = set()
            map_in_end_exclusive = source + map_range_length
            map_out_end_exclusive = destination + map_range_length
            for r in unmapped_ranges:
                start, range_length = r
                end_exclusive = start + range_length
                left_in = source <= start < map_in_end_exclusive
                right_in = source <= end_exclusive <= map_in_end_exclusive
                if left_in and right_in:
                    new_range = (start - source + destination, range_length)
                    mapped.add(new_range)
                elif left_in:
                    overlap = map_in_end_exclusive - start
                    new_range_in = (map_out_end_exclusive - overlap, overlap)
                    mapped.add(new_range_in)
                    new_range_out = (map_out_end_exclusive, map_range_length - overlap)
                    unmapped.add(new_range_out)
                elif right_in:
                    overlap = end_exclusive - source
                    new_range_in = (destination, overlap)
                    mapped.add(new_range_in)
                    new_range_out = (start, range_length - overlap)
                    unmapped.add(new_range_out)
                else:
                    unmapped.add(r)
            mapped_ranges.update(mapped)
            unmapped_ranges = unmapped

        return mapped_ranges | unmapped_ranges

    return min(l for l, _ in map_ranges(len(mappings ) - 1))                                                                                                                                                                       ]

def get_input(f):
    seeds_to_be_planted = list(map(int, next(f).strip().split(':')[1].strip().split()))
    mappings = []
    mapping = []
    for line in f:
        line = line.rstrip()
        if not line:
            if mapping:
                mappings.append(mapping)
            mapping = []
            next(f)
        else:
            mapping.append(list(map(int, line.split())))
    if mapping:
        mappings.append(mapping)
    return seeds_to_be_planted, mappings

def main():
    with open("input.txt") as f:
        seeds_to_be_planted, mappings = get_input(f)
    # print(part1(seeds_to_be_planted, mappings))
    print(part2(seeds_to_be_planted, mappings))


if __name__ == "__main__":
    main()