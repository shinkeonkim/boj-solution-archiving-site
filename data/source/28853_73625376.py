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
  a, b, c, d = mii()
  
  ans = 0

  a %= 2
  c %= 2
  
  k = min(b, d)
  
  b -= k
  d -= k
  
  k = min(a, b)
  a -= k
  b -= k
  ans += k
  
  k = min(a, d)
  a -= k
  d -= k
  ans += k
  
  k = min(b, c)
  b -= k
  c -= k
  ans += k
  
  k = min(c, d)
  c -= k
  d -= k
  ans += k
  
  k = min(a, c)
  a -= k
  c -= k
  ans += 2 * k
  
  ans += b
  ans += d
  
  p(ans)
  

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()

