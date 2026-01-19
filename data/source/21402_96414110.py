"""
[21402: Фитнесс-клуб](https://www.acmicpc.net/problem/21402)

Tier: Bronze 1 
Category: greedy
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


def solve():
  n, k = mii()

  l = [mii() for _ in range(n)]

  stats = [0] * k

  for to_lock, to_unlock in l:
    chk = [True] * k

    if to_unlock > 0:
      # 최대한 열려있는 것을 계속 열려있게 함.
      for i in range(k):
        if not chk[i]:
          continue
        
        if to_unlock > 0 and stats[i]:
          stats[i] = 1
          to_unlock -= 1
          chk[i] = False
      
    if to_unlock > 0:
      # 잠겨있는 것을 열어야 한다.
      for i in range(k):
        if not chk[i]:
          continue
        
        if to_unlock > 0 and stats[i] == 0:
          stats[i] = 1
          to_unlock -= 1
          chk[i] = False
    
    if to_lock > 0:
      # 최대한 열려있던 것을 잠가야 한다.
      for i in range(k):
        if not chk[i]:
          continue
        
        if to_lock > 0 and stats[i] == 1:
          stats[i] = 0
          to_lock -= 1
          chk[i] = False
  
  print(k - sum(stats))


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
