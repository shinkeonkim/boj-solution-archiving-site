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
  mx = -1
  crt = -1
  ans = 0
  
  n = ii()
  l = mii() + [-1]
  
  for i in range(n + 1):
    here = l[i]
    
    if crt > here:
      if mx < crt:
        ans += 1

    mx = max(mx, crt)
    crt = here
  return ans


if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()
    
    p(f"Case #{t}: {ret}")
