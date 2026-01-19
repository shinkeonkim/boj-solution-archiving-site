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
  H, Y = mii()
  
  D = [0] * (Y + 1)
  
  D[0] = H
  for i in range(1, Y + 1):
    D[i] = max(D[i], D[i - 1] * 21 // 20)
    if i > 2:
      D[i] = max(D[i], D[i - 3] * 6 // 5)
    if i > 4:
      D[i] = max(D[i], D[i - 5] * 27 // 20)
  
  p(D[Y])

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()

