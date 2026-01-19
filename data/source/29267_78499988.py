"""
[29267: Случай с игрой](https://www.acmicpc.net/problem/29267)

Tier: Bronze 4 
Category: arithmetic, implementation, math, simulation
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
  n, k = mii()
  # n: 행동 수, k: 한 상자에 들어있는 탄약 수

  savepoint = 0
  crt = 0

  for _ in range(n):
    action = inp()

    if action == 'save':
      savepoint = crt
    elif action == 'load':
      crt = savepoint
    elif action == 'shoot':
      crt -= 1
    else:
      crt += k

    p(crt)

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()