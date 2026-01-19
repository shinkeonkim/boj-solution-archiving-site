import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  k, n = mii()
  d = [0] * k
  
  i = 0
  
  for _ in range(n):
    crt = ii()
    while crt > 0:

      i %= k
      
      can = min(2 - d[i], crt)
      
      d[i] += can
      crt -= can
      i += 1
      
  print(*d,sep="\n")
      
    
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
