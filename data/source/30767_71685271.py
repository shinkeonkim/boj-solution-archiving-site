import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  n = ii()
  a = ii()
  b = ii()
  
  x = ii()
  y = ii()

  k = (n - b, n - a)
  k2 = (x, y)
  
  return max(0, min(k[1], k2[1]) - max(k[0], k2[0]) + 1)
  
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
    p(ret)