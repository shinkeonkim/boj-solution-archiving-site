import sys
from math import sqrt, pi, sin, factorial, ceil, floor

BLANK = " "

inp = input
# inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  n = ii()
  mn = 1111111111111111111
  for i in range(1, 1000):
    for j in range(1, n // i + 1):
      for k in range(1, n // (i * j) + 1):
        if i * j * k > n:
          break
        if i * j * k != n:
          continue
        
        d = i * j * 2 + j * k * 2 + i * k * 2
        mn = min(mn, d)
  p(mn)
        
  
  
if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()
   