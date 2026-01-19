"""
[7361: Currency Exchange](https://www.acmicpc.net/problem/7361)

Tier: Bronze 1 
Category: arithmetic, math
"""


from decimal import Decimal
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
  exchange_rates = [[*map(float, input().split())] for _ in range(5)]
  
  while 1:
    s = input()
    
    if s == '0':
      break
    
    n, *l, money = s.split()
    n = int(n)
    money = float(money)
    
    l = [1] + [*map(int, l)] + [1]
    
    for i in range(1, len(l)):
      first = l[i - 1] - 1
      second = l[i] - 1
      
      exchange_rate = exchange_rates[first][second]
      money *= exchange_rate
      money = round(money, 2)

    print(f"{money:.2f}")


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
