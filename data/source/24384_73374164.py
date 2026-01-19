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
  MX = 99999
  s = ""
  for i in range(1, MX):
    j = i ** 3
    s += str(j)
  p(s[ii() - 1])
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
    
