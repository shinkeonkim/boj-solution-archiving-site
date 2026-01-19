"""
[34419: Tic-Tac-Toe Solver](https://www.acmicpc.net/problem/34419)

Tier: Bronze 2
Category: implementation, case_work
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

def winnable(board, c):
  if all(board[i][i] == c for i in range(3)):
    return True
  
  if all(board[i][2 - i] == c for i in range(3)):
    return True
  
  for i in range(3):
    if all(board[i][j] == c for j in range(3)):
      return True
    
    if all(board[j][i] == c for j in range(3)):
      return True
  
  return False


def solve():
  board = [inp() for _ in range(3)]
  
  o = winnable(board, 'O')
  x = winnable(board, 'X')
  
  if o == x:
    print("N")
    return
  
  if o:
    print("O")

  if x:
    print("X")  


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
