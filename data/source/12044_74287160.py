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
  n, k = mii()
  
  l = [mii() for _ in range(4)]
  
  crt = l[0]
  
  for i in range(1, 4):
    nxt = []  
    for x in crt:
      for y in l[i]:
        nxt.append(x ^ y)
    crt = [*nxt]
  
  return crt.count(k)
  
  
  
if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()
    
    p(f"Case #{t}: {ret}")
