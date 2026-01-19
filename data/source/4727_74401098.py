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
  while 1:
    n, a, b, c = mii()
    
    if n == a == b == c:
      break
    
    mn = (a - 0.5) * 9 + (max(b - 0.5, 0) + max(c - 0.5, 0)) * 4
    mx = (a + 0.5) * 9 + (b + c + 1) * 4
    
    if mn < n < mx:
      p("yes")
    else:
      p("no")
  
  
tc = 1

for t in range(1, tc+1):
  ret = solve()
  
