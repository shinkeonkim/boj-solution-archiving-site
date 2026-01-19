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
  l = [mii() for _ in range(n)]
  
  mn = (0, 111111111)
  
  for w, price in l:
    if w * mn[1] > mn[0] * price:
      mn = (w, price)
    elif w * mn[1] == mn[0] * price:
      if mn[1] > price:
        mn = (w, price)

  p(mn[1])
        
    
if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()
