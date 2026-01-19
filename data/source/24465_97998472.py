"""
[24465: 데뷔의 꿈](https://www.acmicpc.net/problem/24465)

Tier: Silver 4 
Category: implementation, sorting
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

def constellation_number(m, d):
  constellation = [20, 19, 21, 20, 21, 22, 23, 23, 23, 23, 23, 22]
  
  for i in range(12):
    if m == i + 1 and constellation[i] <= d:
      return i + 1
    
    next_i = (i + 2)
    if next_i == 13:
      next_i = 1
    if m == next_i and d < constellation[(i + 1 ) % 12]:
      return i + 1


def solve():
  members = []
  for i in range(7):
    members.append(constellation_number(*mii()))
  
  m = ii()
  ans = []
  for _ in range(m):
    m, d = mii()
    number = constellation_number(m, d)

    if number in members:
      continue
    ans.append((m, d))
  
  ans.sort()
  if len(ans) == 0:
    print("ALL FAILED")
  else:
    for m, d in ans:
      p(m, d)

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
