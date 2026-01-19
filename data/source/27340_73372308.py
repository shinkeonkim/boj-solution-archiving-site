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
  n, m = mii()
  
  l = [i // 4 for i in mii()]
  
  if l.count(0) > 0 or sum(l) < n or n < m:
    print("NE")
  else:
    print("DA")


if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
    
