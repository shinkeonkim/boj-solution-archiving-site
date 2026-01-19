import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta

BLANK = " "

inp = input
# inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def sign(a):
  return a < 0

def solve():
  W, H, N = mii()
  
  a, b = mii()
  k = 0

  for _ in range(N - 1):
    x, y = mii()
    
    if sign(x - a) == sign(y - b):
      i = abs(x - a)
      j = abs(y - b)
      k += max(i, j)
    else:
      k += abs(x - a) + abs(y - b)
    a = x
    b = y
  p(k)
  

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()

