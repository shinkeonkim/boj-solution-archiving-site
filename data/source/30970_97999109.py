"""
[30970: 선택의 기로](https://www.acmicpc.net/problem/30970)

Tier: Silver 4 
Category: sorting
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

def solution_1(l):
  l.sort(key=lambda x: (-x[0], x[1]))
  print(l[0][0], l[0][1], l[1][0], l[1][1])

def solution_2(l):
  l.sort(key=lambda x: (x[1], -x[0]))
  print(l[0][0], l[0][1], l[1][0], l[1][1])

def solve():
  n = ii()
  l = [mii() for _ in range(n)]
  
  solution_1(l)
  solution_2(l)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
