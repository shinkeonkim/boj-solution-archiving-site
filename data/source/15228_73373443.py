import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta

BLANK = " "

# inp = input
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

memo = [-1] * 100000

def f(n):
  global memo
  
  if memo[n] >= 0:
    return memo[n]
  
  if n <= 1:
    memo[n] = 1
    
    return memo[n]
  
  A = n
  B = 1 + max(f(n // 2), f(n // 2 + n % 2))
  
  memo[n] = min(A, B)
  
  return memo[n]


def solve():
  p(f(ii()))
  

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
    
