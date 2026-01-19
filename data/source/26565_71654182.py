import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  n, s = mii()
  l = mii()
  
  k = s * max(l)
  
  return k // 1000 + int(k % 1000 > 0)
  
if __name__ == "__main__":
  tc = ii()
  
  for t in range(1, tc+1):
    ret = solve()
    
    p(ret)
