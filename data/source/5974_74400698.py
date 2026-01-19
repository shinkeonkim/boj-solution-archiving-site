import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta
sys.setrecursionlimit(10**7)

BLANK = " "

# inp = input
inp = lambda : sys.stdin.readline().rstrip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  L, C, N = mii()
  
  ar = [mii() for _ in range(C)] # s: len, p: pos
  
  for s, pos in ar:
    p(abs(pos - N) + s)
  
tc = 1

for t in range(1, tc+1):
  ret = solve()
  
