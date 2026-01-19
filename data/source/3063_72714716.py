import sys
from math import sqrt, pi, sin, factorial, ceil, floor

BLANK = " "

inp = input
# inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  l = mii()
  
  x = (max(l[0], l[4]), min(l[2], l[6]))
  y = (max(l[1], l[5]), min(l[3], l[7]))
  
  x = max(0, x[1] - x[0])
  y = max(0, y[1] - y[0])

  p((l[2] - l[0]) * (l[3] - l[1]) - x * y)
  
if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()