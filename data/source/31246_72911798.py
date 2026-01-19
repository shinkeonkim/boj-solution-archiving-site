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
  
  s = 0
  e = 11111111111111111111111111
  ans = e
  
  l = [mii() for _ in range(n)]
  
  while s <= e:
    X = (s + e) // 2
    
    cnt = 0
    
    for a, b in l:
      if a + X >= b:
        cnt += 1
    
    if cnt >= k:
      ans = min(ans, X)
      e = X - 1
    else:
      s = X + 1
  p(ans)
  
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
    
