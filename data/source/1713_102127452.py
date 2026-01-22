"""
[1713: 후보 추천하기](https://www.acmicpc.net/problem/1713)

Tier: Silver 1
Category: implementation, set, simulation
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
def transpose(matrix): return list(map(list, zip(*matrix)))
def arithmetic_seq_sum(a, n, d): return (a * n + n * (n - 1) * d  // 2)

INF = 123456789

def solve():
  N = ii()
  
  total = ii()
  votes = mii()
  
  votes_count = [0] * (total + 1)
  last_votes = [INF] * (total + 1)
  
  ans = []
  
  for i in range(total):
    current = votes[i]
    
    if current in ans:
      votes_count[current] += 1
      continue
    
    
    if len(ans) == N:
      ans.sort(key=lambda t : (votes_count[t], last_votes[t]))
      votes_count[ans[0]] = 0
      last_votes[ans[0]] = INF
      
      ans = ans[1:]
      
    ans.append(current)
    votes_count[current] = 1
    last_votes[current] = i

  print(*sorted(ans))

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
