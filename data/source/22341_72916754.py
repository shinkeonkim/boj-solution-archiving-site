import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from decimal import Decimal
BLANK = " "

# inp = input
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  n, k = mii()
  
  l = [mii() for _ in range(k)]
  
  d = [n, n]
  
  for x, y in l:
    if d[0] <= x or d[1] <= y:
      continue
    
    left1 = x * d[1]
    left2 = d[0] * y
    
    if left1 >= left2:
      d = [x, d[1]]
    else:
      d = [d[0], y]

  p(d[0] * d[1])
  
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
    
