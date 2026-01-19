import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta

BLANK = " "

inp = input
# inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  a = list(input())
  b = list(input())
  
  mx = 0
  mn = int("1" * 5000)

  for i in range(len(a)):
    z = a[i:] + a[:i]
    
    if z[0] == '0':
      continue
    
    mx = max(mx, int("".join(z)))

  for i in range(len(b)):
    z = b[i:] + b[:i]
    
    if z[0] == '0':
      continue
    
    mn = min(mn, int("".join(z)))
  
  p(mx - mn)
  

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()

