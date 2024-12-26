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
        result = f(*args, **kwargs)
        print(time.perf_counter() - start)
        return result
    return new_f


def main():
    with open("input.txt") as f:
        disk = tuple(map(int, f.read().rstrip()))
    print("Part 1")
    print(part1(disk))
    print()
    print("Part 2: Naive")
    print()
    print(part2(disk))
    print("Part 2: SegTree")
    print()
    print(part2_segtree(disk))
    print("Part 2: SortedList")
    print()
    print(part2_sortedlist(disk))


@bench
def part1(disk):
    files = [disk[i] for i in range(0, len(disk), 2)]
    empty = [disk[i] for i in range(1, len(disk), 2)]
    start, end = 0, len(files) - 1
    new_disk = []
    while start <= end:
        new_disk.extend([start] * files[start])
        start += 1
        if start >= end:
            new_disk.extend([end] * files[end])
            break
        for _ in range(empty[start - 1]):
            while files[end] == 0:
                end -= 1
            new_disk.append(end)
            files[end] -= 1
    return sum(i * val for i, val in enumerate(new_disk))

@bench
def part2(disk):
    chunk_size = disk
    at_chunk = [[] for _ in range(len(chunk_size))]
    chunk_of = {}
    filled = Counter()
    file_size = {}
    for file_id, chunk in enumerate(range(0, len(disk), 2)):
        at_chunk[chunk] = [file_id]
        chunk_of[file_id] = chunk
        filled[chunk] = chunk_size[chunk]
        file_size[file_id] = chunk_size[chunk]
    for file_id in reversed(file_size):
        for chunk in range(chunk_of[file_id]):
            space = chunk_size[chunk] - filled[chunk]
            if space >= file_size[file_id]:
                break
        else:
            continue
        at_chunk[chunk_of[file_id]].remove(file_id)
        at_chunk[chunk].append(file_id)
        filled[chunk_of[file_id]] -= file_size[file_id]
        filled[chunk] += file_size[file_id]
    new_disk = []
    for chunk in range(len(disk)):
        for file_id in at_chunk[chunk]:
            new_disk.extend([file_id] * file_size[file_id])
        unfilled = chunk_size[chunk] - filled[chunk]
        new_disk.extend([0] * unfilled)
    return sum(i * val for i, val in enumerate(new_disk))


@bench
def part2_segtree(disk):
    chunk_size = disk
    at_chunk = [[] for _ in range(len(chunk_size))]
    chunk_of = {}
    filled = Counter()
    file_size = {}
    for file_id, chunk in enumerate(range(0, len(disk), 2)):
        at_chunk[chunk] = [file_id]
        chunk_of[file_id] = chunk
        filled[chunk] = chunk_size[chunk]
        file_size[file_id] = chunk_size[chunk]
    space = lambda chunk: chunk_size[chunk] - filled[chunk]
    max_tree = MaxSegmentTree(range(len(disk)), key=space)
    for file_id in reversed(file_size):
        chunk = max_tree.get_first(file_size[file_id], r=chunk_of[file_id]-1)
        at_chunk[chunk_of[file_id]].remove(file_id)
        at_chunk[chunk].append(file_id)
        filled[chunk_of[file_id]] -= file_size[file_id]
        filled[chunk] += file_size[file_id]
        max_tree.update(chunk, chunk)
        max_tree.update(chunk_of[file_id], chunk_of[file_id])
    new_disk = []
    for chunk in range(len(disk)):
        for file_id in at_chunk[chunk]:
            new_disk.extend([file_id] * file_size[file_id])
        unfilled = chunk_size[chunk] - filled[chunk]
        new_disk.extend([0] * unfilled)
    return sum(i * val for i, val in enumerate(new_disk))
































    print("Part 1")
    print(part1(file))
    print()
    print("Part 2: Naive")
    print(part2(file))
    print()
    print("Part 2: Segtree")
    print(part2_segtree(file))
    print()
    print("Part 2: SortedList")
    print(part2_sortedlist(file))


#@bench
#def part2(file):
#    chunk_size = file
#    at_chunk = [[] for _ in range(len(chunk_size))]
#    file_chunk = {}
#    file_size = {}
#    filled = Counter()
#    for file_id, chunk in enumerate(range(0, len(file), 2)):
#        at_chunk[chunk] = [file_id]
#        file_chunk[file_id] = chunk
#        file_size[file_id] = chunk_size[chunk]
#        filled[chunk] = chunk_size[chunk]
#    for file_id in reversed(range(len(file_chunk))):
#        for chunk in range(file_chunk[file_id]):
#            space = chunk_size[chunk] - filled[chunk]
#            if space >= file_size[file_id]:
#                break
#        else:
#            continue
#        at_chunk[file_chunk[file_id]].remove(file_id)
#        at_chunk[chunk].append(file_id)
#        filled[file_chunk[file_id]] -= file_size[file_id]
#        filled[chunk] += file_size[file_id]
#    new_disk = []
#    for chunk in range(len(chunk_size)):
#        for file_id in at_chunk[chunk]:
#            new_disk.extend([file_id] * file_size[file_id])
#        unfilled = chunk_size[chunk] - filled[chunk]
#        new_disk.extend([0] * unfilled)
#    return sum(i * file_id for i, file_id in enumerate(new_disk))

@bench
def part2_sortedlist(file):
  pos_at = list(accumulate(file))
  unfilled_with_size = [SortedList() for _ in range(10)]
  for i in range(1, len(file), 2):
      unfilled_with_size[file[i]].add(i)
  total = 0
  for i in range(len(file) - 1, 0, -2):
    file_id = i // 2
    space_found, j = 0, i - 1
    for size in range(file[i], 10):
      indices = unfilled_with_size[size]
      if indices and indices[0] <= j:
        space_found = size
        j = indices[0]
    unfilled_with_size[space_found].discard(j)
    total += file_id * file[i] * (2 * (pos_at[j] - space_found) + (file[i] - 1)) // 2
    unfilled_with_size[space_found - file[i]].add(j)
    for indices in unfilled_with_size:
      indices.discard(i-1)
  return total



if __name__ == "__main__":
    main()
