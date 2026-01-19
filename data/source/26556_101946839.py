"""
[26556: Bags](https://www.acmicpc.net/problem/26556)

Tier: Silver 2
Category: bruteforcing, backtracking
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
SET_RECURSION = True
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
def transpose(matrix): return list(map(list, zip(*matrix)))
def arithmetic_seq_sum(a, n, d): return (a * n + n * (n - 1) * d  // 2)

n = 0
l = []
k = 0

INF = 1e18

def f(idx, left, cnt):
  if idx == 0:
    if left == 0:
      return cnt
    if l[idx] == left:
      return cnt + 1
    return INF
  
  ret = f(idx - 1, left, cnt)
  
  if left - l[idx] >= 0:
    ret = min(ret, f(idx - 1, left - l[idx], cnt + 1))
    
  return ret


def solve():
  global n, l, k
  n = ii()
  l = mii()
  k = ii()
  
  return f(n - 1, k, 0)


if __name__ == "__main__":
  tc = ii()
  for t in range(1, tc+1):
    ret = solve()
    print("Not possible" if ret == INF else ret)
