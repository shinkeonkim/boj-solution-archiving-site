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
  m, n = mii()
  l = [mii() for _ in range(n)]
  
  for i in range(m):
    for j in range(1, n):
      l[0][i] *= l[j][i]
  
  mx = max(l[0])
  
  for i in range(m - 1, -1, -1):
    if l[0][i] == mx:
      p(i + 1)
      break
  
if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()
    
