import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  w, h = mii()
  
  x = y = 0
  
  while 1:
    a, b = mii()
    
    if a == b == 0:
      break
    
    x += a
    y += b
    
    x = max(x, 0)
    y = max(y, 0)
    
    x = min(x, w)
    y = min(y, h)
    print(x, y)
    
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
