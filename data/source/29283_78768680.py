"""
[29283: Алекс и стейк](https://www.acmicpc.net/problem/29283)

Tier: Bronze 3 
Category: arithmetic, math
"""

import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta

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
  k = ii()

  mx_cnt = (k - 1) // 5 + 1
  last = k % 5 
  if last == 0:
    last = 5

  idx = mx_cnt - 1

  ans = idx * (idx + 1) // 2 * 5 * 30
  ans += last * mx_cnt * 30

  p(ans)

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()