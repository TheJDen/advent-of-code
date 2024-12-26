from collections import *
from itertools import *
from functools import *
import re
from string import *
from heapq import *
import time
import operator
from math import *

def main():
    with open("input.txt") as f:
        connections = [line.rstrip().split("-") for line in f]
    print(part1(connections))
    print(part2(connections))

def part1(connections):
    adj = defaultdict(set)
    for a, b in connections:
        adj[a].add(b)
        adj[b].add(a)
    bruh = set()
    for i, ci in adj.items():
        for j in ci:
            for k in adj[j]:
                if i == k or i not in adj[k]:
                    continue
                if any(c.startswith("t") for c in (i, j, k)):
                    bruh.add(tuple(sorted([i, j, k])))
    return len(bruh)

def part2(connections):
    adj = defaultdict(set)
    for a, b in connections:
        adj[a].add(b)
        adj[b].add(a)
    cliques = []
    for start in adj:
        clique = {start}
        remaining = set(adj) - clique
        while remaining:
            candidate = remaining.pop()
            if all(candidate in adj[c] for c in clique):
                clique.add(candidate)
        cliques.append(clique)
    best = max(cliques, key=len)
    return ",".join(sorted(best))



if __name__ == "__main__":
    main()
