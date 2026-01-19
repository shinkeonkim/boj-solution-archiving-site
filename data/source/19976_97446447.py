"""
[19976: Профессор Хаос](https://www.acmicpc.net/problem/19976)

Tier: Bronze 1 
Category: implementation, simulation
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
  a, b, c, d, k = mii()
  # a : 시작 개수
  # b : 각 박테리아는 b개의 새로운 박테리아로 변함
  # c : 인큐베이터에서 박테리아를 꺼낸 뒤, 그 중 c개는 각종 시럼에 사용 후 폐기
  # d : d개만 남기고 폐기함.
  
  current = a
  timing = {}
  values = {}
  timing[current] = 0
  values[0] = current
  for i in range(1, k + 1):
    current = min(max(0, current * b - c), d)
    
    if current == 0:
      print(0)
      return
    values[i] = current
    
    if timing.get(current, -1) != -1:
      period = i - timing[current]
      remaining = (k - i) % period
      print(values[timing[current] + remaining])
      return
    timing[current] = i
  
  print(current)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
