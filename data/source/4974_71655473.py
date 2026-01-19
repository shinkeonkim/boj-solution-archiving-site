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
  
  if n == 0:
    return
  
  l = [ii() for _ in range(n)]
  
  return (sum(l) - max(l) - min(l)) // (n - 2)
  
  
if __name__ == "__main__":
  tc = 11111111111111111
  
  for t in range(1, tc+1):
    ret = solve()
    
    if ret == None:
      break
    
    p(ret)
