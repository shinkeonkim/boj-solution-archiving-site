"""
[23056: 참가자 명단](https://www.acmicpc.net/problem/23056)

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
from dataclasses import dataclass

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

@dataclass
class Student:
  class_number: int
  name: str
  team_number: int
  
  def __lt__(self, other):
    if self.team_number != other.team_number:
      return self.team_number < other.team_number

    if self.class_number != other.class_number:
      return self.class_number < other.class_number

    if len(self.name) != len(other.name):
      return len(self.name) < len(other.name)

    return self.name < other.name


def solve():
  n, m = mii()
  
  students = []
  c = Counter()
  while 1:
    s = input()
    
    if s == '0 0':
      break
  
    class_number, name = s.split()
    class_number = int(class_number)
    
    if c[class_number] >= m:
      continue
    
    c[class_number] += 1
    students.append(Student(class_number, name, 1 - class_number % 2))
  students.sort()
  
  for student in students:
    print(student.class_number, student.name)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
