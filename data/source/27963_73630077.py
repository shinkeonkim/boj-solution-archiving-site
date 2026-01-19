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


def solve():
  d1, d2, X = mii()
  
  if d1 > d2:
    d1, d2 = d2, d1
  
  w1 = d1 * d2 * X
  w2 = d1 * d2 * (100 - X)
  
  v1 = w1 // d2
  v2 = w2 // d1

  p((w1 + w2) / (v1 + v2))

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()

