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
  n = ii()
  prev = fi()
  
  rng = [30, 4000]
  
  l = [input().split() for _ in range(n - 1)]
  
  for _ in range(n - 1):
    crt, msg = l[_]
    crt = float(crt)
    dis = abs(prev - crt)
    
    if crt == prev:
      continue
    
    if msg == 'closer':
      if crt < prev:
        rng[1] = min(rng[1], crt + dis / 2)
      else:
        rng[0] = max(rng[0], crt - dis / 2)
    else:
      if crt < prev:
        if prev - dis / 2 <= rng[1]:
          rng[0] = max(rng[0], prev - dis / 2)
      else: # prev < a
        if prev + dis / 2 >= rng[0]:
          rng[1] = min(rng[1], prev + dis / 2)
    # rng[0] = max(30, rng[0])
    # rng[1] = min(4000, rng[1])
    prev = crt

  for i in rng:
    p(f"{i:.6f}", end=" ")

    
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
