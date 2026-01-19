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


def solve():
  x, n = mii()
  
  d, m, y = mii()
  
  diff = (x - 1) * 2 * n + n - 1
  
  ret = datetime(year=y, month=m, day=d) + timedelta(diff)
  
  p(ret.day, ret.month, ret.year)

  
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
