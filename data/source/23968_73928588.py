import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta

BLANK = " "

#inp = input
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  n, k = mii()
  
  l = mii()
  cnt = 0  
  for last in range(n - 1, 0, -1):
    for i in range(0, last):
      if l[i] > l[i + 1]:
        l[i], l[i + 1] = l[i + 1], l[i]
        cnt += 1
        
        if cnt == k:
          p(l[i], l[i + 1])
          return
  p(-1)
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
