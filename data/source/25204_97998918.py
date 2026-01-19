"""
[25204: 문자열 정렬](https://www.acmicpc.net/problem/25204)

Tier: Silver 4 
Category: implementation, string, sorting
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


def solve():
  n = ii()
  l = [inp() for _ in range(n)]
  l2 = []
  for s in l:
    ret = []
    for i in s:
      if i == '-':
        ret.append(ord('{'))
      elif i.islower():
        ret.append((ord(i) - ord('a')) * 2 + 1)
      else:
        ret.append((ord(i) - ord('A')) * 2)
    l2.append(ret)
  
  l2.sort()
  
  for i in l2:
    ret = ""
    for j in i:
      if j == ord('{'):
        ret += '-'
      else:
        if j % 2 == 0:
          ret += chr(j // 2 + ord('A'))
        else:
          ret += chr(j // 2 + ord('a'))
    p(ret)

if __name__ == "__main__":
  tc = ii()
  for t in range(1, tc+1):
    ret = solve()
