"""
[9979: Does This Make Me Look Fat?](https://www.acmicpc.net/problem/9979)

Tier: Silver 5 
Category: implementation, string, sorting, parsing
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

class Person:
  name: str
  weight: int
  
  def __init__(self, name: str, duration: int, start_weight: int):
    self.name = name
    self.weight = start_weight - duration
    
  def __lt__(self, other):
    return self.weight < other.weight


def solve():
  while 1:
    try:
      start = input()
    except EOFError:
      break
    
    persons = []
  
    while 1:
      line = input()
      if line == 'END':
        break
      
      name, duration, start_weight = line.split()
      duration = int(duration)
      start_weight = int(start_weight)
      
      persons.append(Person(name, duration, start_weight))
      
    persons.sort(reverse=True)
    for person in persons:
      print(person.name)
    print()
      


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
