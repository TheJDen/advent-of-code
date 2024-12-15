from collections import *
from itertools import *
from functools import *
from string import *
from heapq import *
import time
import operator
from segment_tree import *
from sortedcontainers import *

def bench(f):
    def new_f(*args, **kwargs):
        start = time.perf_counter()
        ret = f(*args, **kwargs)
        print("Seconds: ", time.perf_counter() - start)
        return ret
    return new_f

def main():
    with open("input.txt") as f:
        file = tuple(map(int, f.read().rstrip()))
    print("Part 1")
    print(part1(file))
    print()
    print("Part 2: Naive")
    print(part2(file))
    print()
    print("Part 2: Optimized")
    print(part3(file))

@bench
def part1(file):
    remaining_blocks = [file[i] for i in range(0, len(file), 2)]
    empty = [file[i] for i in range(1, len(file), 2)]
    start, end = 0, len(remaining_blocks) - 1
    new_disk = []
    while start <= end:
        new_disk.extend([start] * remaining_blocks[start])
        remaining_blocks[start] = 0
        start += 1
        if start >= end:
            new_disk.extend([end] * remaining_blocks[end])
            break
        for _ in range(empty[start - 1]):
            while not remaining_blocks[end]:
                end -= 1
            new_disk.append(end)
            remaining_blocks[end] -= 1
    return sum(i * file_id for i, file_id in enumerate(new_disk))

@bench
def part2(file):
    chunk_size = file
    at_chunk = [[] for _ in range(len(chunk_size))]
    file_chunk = {}
    file_size = {}
    filled = Counter()
    for file_id, chunk in enumerate(range(0, len(file), 2)):
        at_chunk[chunk] = [file_id]
        file_chunk[file_id] = chunk
        file_size[file_id] = chunk_size[chunk]
    for file_id in reversed(range(len(file_chunk))):
        for chunk in range(file_chunk[file_id]):
            space = chunk_size[chunk] - filled[chunk]
            if space >= file_size[file_id]:
                break
        else:
            continue
        at_chunk[file_chunk[file_id]].pop()
        at_chunk[chunk].append(file_id)
        filled[chunk] += file_size[file_id]
        file_chunk[file_id] = chunk
    new_disk = []
    for chunk in range(len(chunk_size)):
        for file_id in at_chunk[chunk]:
            new_disk.extend([file_id] * file_size[file_id])
        unfilled = chunk_size[chunk] - sum(file_size[fi] for fi in at_chunk[chunk])
        new_disk.extend([0] * unfilled)
    return sum(i * file_id for i, file_id in enumerate(new_disk))

@bench
def part3(file):
    chunk_size = file
    at_chunk = [[] for _ in range(len(chunk_size))]
    file_chunk = {}
    file_size = {}
    filled = Counter()
    for file_id, chunk in enumerate(range(0, len(file), 2)):
        at_chunk[chunk] = [file_id]
        file_chunk[file_id] = chunk
        file_size[file_id] = chunk_size[chunk]
    space = lambda chunk: chunk_size[chunk] - filled[chunk]
    max_tree = MaxSegmentTree(list(range(len(at_chunk))), space)
    for file_id in reversed(range(len(file_chunk))):
        chunk = max_tree.get_first(file_size[file_id], r=file_chunk[file_id] - 1)
        if chunk == file_chunk[file_id]:
            continue
        at_chunk[file_chunk[file_id]].pop()
        at_chunk[chunk].append(file_id)
        filled[chunk] += file_size[file_id]
        file_chunk[file_id] = chunk
        max_tree.update(file_chunk[file_id], file_chunk[file_id])
        max_tree.update(chunk, chunk)
    new_disk = []
    for chunk in range(len(chunk_size)):
        for file_id in at_chunk[chunk]:
            new_disk.extend([file_id] * file_size[file_id])
        unfilled = chunk_size[chunk] - sum(file_size[fi] for fi in at_chunk[chunk])
        new_disk.extend([0] * unfilled)
    return sum(i * file_id for i, file_id in enumerate(new_disk))



if __name__ == "__main__":
    main()
