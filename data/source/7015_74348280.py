import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta
sys.setrecursionlimit(10**7)

BLANK = " "

#inp = input
inp = lambda : sys.stdin.readline().rstrip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  Y, M, D = mii()
  y, m, d = 1000, 1, 1
  
  cnt = 0

  while Y != y or M != m or D != d:
    cnt += 1
    D += 1

    if Y % 3 == 0:
      if D == 21:
        D = 1
        M += 1
    else:
      if M % 2 == 1:
        if D == 21:
          D = 1
          M += 1
      else:
        if D == 20:
          D = 1
          M += 1
      
    if M == 11:
      M = 1
      Y += 1
  return cnt


if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()
      
    p(ret)
