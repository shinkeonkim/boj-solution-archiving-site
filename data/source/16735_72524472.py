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
  l = [input() for _ in range(n)]
  
  d = [
    [390, 600, 390, 960, 24000],
    [390, 600, 961, 1140, 36000],
    [601, 960, 601, 960, 16800],
    [601, 1140, 961, 1140, 24000]
  ]
  
  mn = 1111111111
  mx = 0
  for i in l:
    h, m = map(int, i.split(":"))
    
    t = h * 60 + m
    
    if 390 <= t <= 1140:
      mn = min(mn, t)
      mx = max(mx, t)
  
  for a, b, c, d, price in d:
    if a <= mn <= b and c <= mx <= d:
      p(price)
      break
  else:
    p(0)
    
  
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
   