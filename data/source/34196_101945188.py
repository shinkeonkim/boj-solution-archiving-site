"""
[34196: SUAPC 2025 Winter](https://www.acmicpc.net/problem/34196)

Tier: Silver 5
Category: implementation, precomputation
"""


import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta
from collections import deque, defaultdict, Counter
from itertools import permutations, combinations, product
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify
from functools import reduce, lru_cache
from operator import itemgetter, attrgetter, mul, add, sub, truediv
from typing import List, Tuple, Dict, Set, Any, Union
from fractions import Fraction

SYS_INPUT = True
RECURSION_LIMIT = 10 ** 7
SET_RECURSION = False
BLANK = " "
INF = 1e10

if SET_RECURSION:
  sys.setrecursionlimit(RECURSION_LIMIT)

inp = lambda : sys.stdin.readline().rstrip() if SYS_INPUT else input()
mii = lambda : [*map(int,inp().split())]
mfi = lambda : [*map(float,inp().split())]
ii = lambda : int(inp())
fi = lambda : float(inp())
isplit = lambda : inp().split()
p = print

def gcd(a, b): return gcd(b, a % b) if b > 0 else a
def lcm(a, b): return a * b // gcd(a, b)
def near_integer(x): return int(x + 0.5) if x >= 0 else int(x - 0.5)
def round_up_half(n): return floor(n + 0.5)
def rotate90(l): return [''.join(x) for x in zip(*l[::-1])]
def transpose(matrix): return list(map(list, zip(*matrix)))
def arithmetic_seq_sum(a, n, d): return (a * n + n * (n - 1) * d  // 2)

l = [
  [],
  [0, 0, 0, 2, -1, 0, 2, 0, 0, 3, 2, 1, 0],
  [0, 1, 0, 0, -8, 0, 4, 3, 2, 0, 2, 3, 3],
  [0, 0, 0, 1, -1, 0, -2, 3, 0, 0, 1, 1, 0],
  [0, 0, 0, 3, INF, 0, INF, 0, 1, 0, 1, 1, 0],
  [0, 1, 1, 0, INF, 0, INF, 6, 4, 0, 1, 0, 1],
  [0, 2, 1, 0, INF, 0, INF, 1, 1, 0, 5, 0, 0],
  [0, 3, 1, -1, INF, 0, INF, -7, 0, 0, 3, 1, 1],
  [1, 1, 2, -1, -1, 0, -1, -5, 0, 0, 5, 0, 0],
  [0, 1, 0, INF, INF, 0, INF, 2, INF, 1, -2, 0, 0],
  [0, 1, 2, INF, INF, 1, INF, -1, INF, 0, 3, 2, 3],
  [0, 4, 2, INF, INF, 0, INF, -2, INF, 0, -5, 0, INF],
  [0, -5, 0, INF, INF, 0, INF, -2, INF, 0, INF, 2, INF],
  [0, -9, 3, INF, INF, 0, INF, INF, INF, 0, INF, 13, INF],
  [0,-10, 0, INF, INF, 0, INF, INF, INF, 0, INF, 0, INF],
  [0, 0, -8, INF, INF, 0, INF, INF, -2, 0, INF, -1, INF],
  [0, -2, -2, INF, INF, 0, INF, INF, INF, 1, INF, 2, INF],
  [0, -8, -3, INF, INF, 2, INF, INF, INF, 0, INF, 3, INF],
  [0, -8, 3, INF, INF, 0, INF, -3, INF, 4, INF, INF, INF],
  [0, -10, INF, INF, INF, 7, INF, INF, INF, -4, INF, INF, INF],
  [0, -7, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
]

def f(r, c):
  k = l[r][c]
  
  if k == INF:
    print("No 0")
    return
  
  if k >= 0:
    print("Yes", k)
    return

  print("No", -k)
  
def solve():
  for i in l[1:]:
    assert(len(i) == 13)
    
  for _ in range(int(input())):
    r, c = input().split()
    r = int(r)
    c = ord(c) - 65
    
    f(r, c)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
