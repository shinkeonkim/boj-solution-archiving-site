import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from decimal import Decimal
BLANK = " "

inp = input
# inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def f(r, d):
  return 2 / 3 * pi * ((r - d / 2) ** 2) * (2 * r + d / 2)

def g(r):
  return 4 * pi * (r ** 3) / 3

def dis(a, b):
  return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2]- b[2]) ** 2)

def solve():
  n, r = mii()
  ans = 0
  l = [mii() for _ in range(n)]
  
  for i in range(n):
    crt = l[i]
    nxt = l[(i + 1) % n]
    
    d = dis(crt, nxt)
    
    ans += g(r) - f(r, d)
    
  p(ans)
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
    
