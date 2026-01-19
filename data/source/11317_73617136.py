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
  a, b, c, s, t = mii()
  
  z = b * b - 4 * a * c
  z2 = 2 * a
  
  if z < 0:
    p("No")
    return

  x1 = (-b - sqrt(z)) / z2
  x2 = (-b + sqrt(z)) / z2
  
  if s <= x1 <= t or s <= x2 <= t:
    p("Yes")
  else:
    p("No")

    
if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()

