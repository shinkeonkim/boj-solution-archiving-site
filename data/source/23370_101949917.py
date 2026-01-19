"""
[23370: <code>git mv</code>](https://www.acmicpc.net/problem/23370)

Tier: Silver 1
Category: implementation, string, parsing
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

def to_path(l):
  return "/".join(l)

def solve():
  A = input().split("/")
  B = input().split("/")
  
  if A == B:
    print(to_path(A))
    return
  
  s = 0
  e = 0 # 갯수 기준
  N = min(len(A), len(B))
  for i in range(N):
    if A[i] == B[i]:
      s += 1
    else:
      break
  
  for i in range(-1, -N - 1, -1):
    if A[i] == B[i]:
      e += 1
    else:
      break
  
  for i in range(s):
    print(A[i]+"/",end="")
  
  k1 = A[s:(-e)] if e != 0 else A[s:]
  k2 = B[s:(-e)] if e != 0 else B[s:]
  
  print(f"{{{to_path(k1)} => {to_path(k2)}}}", end="")
  
  for i in range(-e, 0, 1):
    print("/"+A[i], end="")

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
