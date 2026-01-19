"""
[27240: Электричка](https://www.acmicpc.net/problem/27240)

Tier: Bronze 4 
Category: implementation, math
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
  n, a, b = mii()
  s, t = mii()
    
  s, t = min(s, t), max(s, t)

  if a + 1 <= s and t <= b - 1:
    print("City")
  elif t <= a or b <= s:
    print("Outside")
  else:
    print("Full")


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()