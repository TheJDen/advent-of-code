import pathlib
from sortedcontainers import SortedList
from itertools import accumulate


def reader():
  return open(f"{pathlib.Path(__file__).parent.resolve()}/input.txt", 'r').read().split('\n')[:-1]


def part1():
  n = list(map(int, reader()[0]))
  s = []
  c = 0
  i = 0
  j = len(n) - 1
  while i <= j:
    if i % 2 == 0:
      a = i // 2
      for _ in range(n[i]):
        s.append(a)
        c += 1
    else:
      ii = 0
      while i < j and ii < n[i]:
        if n[j] == 0 or j % 2 != 0:
          j -= 1
        else:
          a = j // 2
          s.append(a)
          c += 1
          n[j] -= 1
          ii += 1
    i += 1
  print(sum(i * n for i, n in enumerate(s)))

def part2():
  disk = tuple(map(int, reader()[0]))
  id_at = list(accumulate(disk))
  unfilled_with_size = [SortedList() for _ in range(10)]
  for i in range(1, len(disk), 2):
      unfilled_with_size[disk[i]].add(i)
  total = 0
  for i in range(len(disk) - 1, 0, -2):
    file_id = i // 2
    space_found, j = 0, i - 1
    for size in range(disk[i], 10):
      indices = unfilled_with_size[size]
      if indices and indices[0] <= j:
        space_found = size
        j = indices[0]
    unfilled_with_size[space_found].discard(j)
    total += file_id * disk[i] * (2 * (id_at[j] - space_found) + (disk[i] - 1)) // 2
    unfilled_with_size[space_found - disk[i]].add(j)
    for indices in unfilled_with_size:
      indices.discard(i-1)
  print(total)


# slow ~ 1.3s
def original_part2():
  disk = list(map(int, reader()[0]))
  size = [disk[i] for i in range(0, len(disk), 2)]
  space = [disk[i] for i in range(1, len(disk), 2)]
  contents = [[] for _ in range(len(space))]
  empty = set()
  for file_id in reversed(range(len(size))):
    j = next((j for j in range(file_id) if space[j] >= size[file_id]), None)
    if j is None:
        continue
    space[j] -= size[file_id]
    empty.add(file_id)
    contents[j].extend([file_id] * size[file_id])
  new_disk = []
  for file_id, s in enumerate(size):
    new_disk.extend([file_id if file_id not in empty else 0] * s)
    if file_id < len(contents):
        new_disk.extend(contents[file_id] + [0] * space[file_id])
  print(sum(i * n for i, n in enumerate(new_disk)))


part1()
part2()
original_part2()
