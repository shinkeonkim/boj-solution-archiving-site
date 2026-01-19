"""
[2792: 보석 상자](https://www.acmicpc.net/problem/2792)

Tier: Silver 1 
Category: binary_search, parametric_search

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
  N, M = mii() # N: 학생 수, M : 색상의 수
  
  l = [ii() for _ in range(M)]

  left = 1
  right = 10000000000

  ans = 10000000000

  while left <= right:
    mid = (left + right) // 2
    
    cnt = 0
    for i in l:
      cnt += (i + mid - 1) // mid

    if cnt <= N:
      ans = min(ans, mid)
      right = mid - 1
    else:
      left = mid + 1
  
  p(ans)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()