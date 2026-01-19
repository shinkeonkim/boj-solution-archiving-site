import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta
# sys.setrecursionlimit(10**7)

BLANK = " "

# inp = input
inp = lambda : sys.stdin.readline().rstrip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

  
def solve():
  n = ii()
  l = mii()
  
  crt = 1
  
  for i in l:
    while i == crt:
      crt += 1
    crt += 1
  p(crt - 1)


if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()
