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
  n = ii()
  l = [ii() for _ in range(n)][::-1]
  mn = l[0]
  crt = l[0]
  d = []
  
  for i in range(1, n):
    if crt <= l[i]:
      crt = l[i]
    else:
      d.append([mn, crt])
      mn = l[i]
      crt = l[i]
  d.append([mn, crt])
  
  s = 100
  for a, b in d:
    s *= b / a
  p(s)
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
    
