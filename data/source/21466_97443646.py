"""
[21466: Жребий Крижановского](https://www.acmicpc.net/problem/21466)

Tier: Bronze 1 
Category: bruteforcing
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

SYS_INPUT = False
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
  n = int(input())
  scores = [*map(int, input().split())]
  numbers = [*map(int, input().split())]
  
  ans = -1
  ans_cnt = -1
  
  for pecha_number in range(1, 102):
    new_scores = scores[:]
    new_numbers = numbers[:] + [pecha_number]
    
    winner_number = -1
    
    sorted_numbers = sorted(set(new_numbers))

    for number in sorted_numbers:
      if new_numbers.count(number) == 1:
        winner_number = number
        break

    if winner_number != -1:
      for i in range(n):
        if new_numbers[i] == winner_number:
          new_scores[i] += winner_number
    cnt = 0
    for i in range(n - 1):
      if new_scores[-1] > new_scores[i]:
        cnt += 1
    
    if cnt > ans_cnt:
      ans = pecha_number
      ans_cnt = cnt
    
  print(ans)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
