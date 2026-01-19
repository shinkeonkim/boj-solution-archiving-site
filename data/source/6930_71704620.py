import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  x = ii()
  m = ii()
  
  for n in range(100000):
    if (x * n) % m == 1:
      return n
  return "No such integer exists."
  
    
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
    p(ret)