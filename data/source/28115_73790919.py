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
  n = ii()
  l = mii()
  
  if n == 1:
    p("YES")
    p(l[0] + 1)
    p(- 1)
    return
  
  k = l[1] - l[0]
  
  for i in range(1, n - 1):
    if l[i + 1] - l[i] != k:
      p("NO")
      return
  
  p("YES")
  for i in l:
    p(2 * i, end = " ")
  p()
  
  for i in l:
    p(-i, end = " ")
  
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
