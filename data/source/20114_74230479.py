import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta

BLANK = " "

#inp = input
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  N, H, W = mii()
  
  l = [input() for _ in range(H)]
  
  for i in range(N):
    chk = "?"
    for h in range(H):
      for w in range(W):
        if l[h][W * i + w] != '?':
          chk = l[h][W * i + w]
    p(end=chk)

  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
    
