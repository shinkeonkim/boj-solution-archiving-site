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
  l = input().split()

  crt = len(l[0])
  s = l[0]

  for i in l[1:]:
    if crt + len(i) <= k:
      crt += len(i)
      s += " " + i
    else:
      p(s)
      crt = len(i)
      s = i
  p(s)

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()