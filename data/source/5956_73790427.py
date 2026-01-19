import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta

BLANK = " "

#inp = input
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def f(n, m):
  if n <= 0 or m <= 0:
    return 0
  if n % 2 == 0 or m % 2 == 0:
    return 0
  
  if n == 1 and m == 1:
    return 1
  
  if n == 1:
    return 1 + 2 * f(n, (m - 3) // 2)
  
  if m == 1:
    return 1 + 2 * f((n - 3) // 2, m)
  
  return 1 + 4 * f(n // 2, m // 2)

def solve():
  n, m = mii()
  
  p(f(n, m))
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
