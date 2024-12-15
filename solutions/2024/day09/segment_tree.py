from math import *
from typing import *
import operator

class SegmentTree:
    def __init__(self, elements, key=(lambda x: x), bin_op=operator.add, default=0):
        self.n = len(elements)
        self.tree = [default] * (4 * self.n)
        self._bin_op = bin_op
        self._key = key
        self._default = default
        self._build(elements)

    def _build(
            self,
            elements,
            node: Optional[int] = None,
            lo: Optional[int] = None,
            hi: Optional[int] = None
            ):
        node = node if node is not None else 1
        lo = lo if lo is not None else 0
        hi = hi if hi is not None else (self.n - 1)
        if lo == hi:
            self.tree[node] = self._key(elements[lo])
            return
        left, right = 2 * node, 2 * node + 1
        mid = (lo + hi) // 2
        self._build(elements, left, lo, mid)
        self._build(elements, right, mid + 1, hi)
        self.tree[node] = self._bin_op(self.tree[left], self.tree[right])

    def get(
            self,
            l: int,
            r: int,
            node: Optional[int] = None,
            lo: Optional[int] = None,
            hi: Optional[int] = None
            ):
        if l > r:
            return self._default
        node = node if node is not None else 1
        lo = lo if lo is not None else 0
        hi = hi if hi is not None else (self.n - 1)
        if l == lo and r == hi:
            return self.tree[node]
        left, right = 2 * node, 2 * node + 1
        mid = (lo + hi) // 2
        get_left = self.get(l, min(r, mid), left, lo, mid)
        get_right = self.get(max(l, mid + 1), r, right, mid + 1, hi)
        return self._bin_op(get_left, get_right)

    def update(
            self,
            i: int,
            val,
            node: Optional[int] = None,
            lo: Optional[int] = None,
            hi: Optional[int] = None
            ):
        node = node if node is not None else 1
        lo = lo if lo is not None else 0
        hi = hi if hi is not None else (self.n - 1)
        if lo == hi:
            self.tree[node] = self._key(val)
            return
        left, right = 2 * node, 2 * node + 1
        mid = (lo + hi) // 2
        if i <= mid:
            self.update(i, val, left, lo, mid)
        else:
            self.update(i, val, right, mid + 1, hi)
        self.tree[node] = self._bin_op(self.tree[left], self.tree[right])

class MaxSegmentTree(SegmentTree):
    def __init__(self, elements, key=lambda x: x):
        super().__init__(elements, key, max, -inf)

    def get_first(
            self,
            x,
            l: Optional[int] = None,
            r: Optional[int] = None,
            node: Optional[int] = None,
            lo: Optional[int] = None,
            hi: Optional[int] = None
            ):
        node = node if node is not None else 1
        lo = lo if lo is not None else 0
        hi = hi if hi is not None else (self.n - 1)
        l = l if l is not None else 0
        r = r if r is not None else (self.n - 1)
        if lo > r or hi < l or self.tree[node] < x:
            return r + 1
        if lo == hi:
            return lo
        left, right = 2 * node, 2 * node + 1
        mid = (lo + hi) // 2
        left = self.get_first(x, l, r, left, lo, mid)
        if left != r + 1:
            return left
        return self.get_first(x, l, r, right, mid + 1, hi)

def main():
    nums = (5, 1, 9, 3, 24, 7, 2, 50, 6)
    n = len(nums)
    max_tree = MaxSegmentTree(nums)
    for i in range(n):
        for j in range(i, n):
            true = max(nums[i:j + 1])
            tree = max_tree.get(i, j)
            if true != tree:
                print(i, j, true, tree)
    print("+++++")
    nums = list(nums)
    nums[4] = 0
    nums = tuple(nums)
    max_tree.update(4, 0)
    for i in range(n):
        for j in range(i, n):
            true = max(nums[i:j + 1])
            tree = max_tree.get(i, j)
            if true != tree:
                print(i, j, true, tree)

if __name__ == "__main__":
    main()



        
