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
  l = [input().split() for _ in range(ii())]
  
  l.sort(key = lambda t : (-(2 * int(t[1]) + 3 * int(t[2]) + int(t[3])), t[0]))
  
  for i in range(min(2, len(l))):
    p(l[i][0])
  

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()

