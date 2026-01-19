"""
[32571: Leg Day](https://www.acmicpc.net/problem/32571)

Tier: Bronze 2 
Category: implementation, string
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

REST = 0
LEG = 1
ARM = 2

def solve():
  n = ii()

  d = []
  ch = ["😎", "🦵", "💪"]

  for i in range(n):
    s = inp()

    if "rest" in s:
      d.append(REST)
    elif "leg" in s:
      d.append(LEG)
    else:
      d.append(ARM)
  
  ans = ""
  for i in range(31):
    ans += ch[d[i % n]]
  
  for i in range(5):
    print(i + 1, ans[i * 7 : i * 7 + 7])




if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()