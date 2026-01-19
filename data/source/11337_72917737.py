import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from decimal import Decimal
BLANK = " "

# inp = input
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  r, b = mii()
  
  z = b / 2
  
  z = min(z, r / sqrt(2))
  ans = 4 * z * sqrt(r * r - z * z)
  
  p(f"{ans:.3f}")


if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()
