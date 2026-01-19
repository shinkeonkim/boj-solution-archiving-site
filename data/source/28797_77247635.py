"""
[28797: Дневнегреческая машина](https://www.acmicpc.net/problem/28797)

Tier: Bronze 1
Category: 구현, 수학
"""


import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta
sys.setrecursionlimit(10**7)

BLANK = " "

# inp = input
inp = lambda : sys.stdin.readline().rstrip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def f(A, dis):
  need = dis / 100
  
  mn = A - 3 * need
  
  if mn < 0:
    return 0
  
  mn = min(1, mn)
  
  return (need + mn) * 100

def solve():
  A = fi()
  
  if A <= 1:
    return A * 100
  
  # x: 소모 L
  
  # y: 묻는 정도: 1 - 2 * x
  
  # (A - 1) * 100 + 
  
  
  left = 0
  right = 100
  ans = 100
  
  delta = 0.00000001

  while left <= right:
    lmid = left * 2 / 3 + right / 3
    rmid = left / 3 + right * 2 / 3
    
    x = f(A, lmid)
    y = f(A, rmid)
    
    if x > y:
      ans = max(ans, x)
      right = rmid - delta
    else:
      ans = max(ans, y)
      left = lmid + delta
    
  return ans


if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
    
    p(ret)
