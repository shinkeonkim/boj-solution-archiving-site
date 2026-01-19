import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  t, d, m = mii()
  
  l = sorted([ii() for _ in range(m)] + [d])
  
  if len(l) == 0:
    return ("Y" if d >= t else "N")
  
  z = l[0]

  for i in range(1, len(l)):
    z = max(z, l[i] - l[i - 1])
  
  return ("Y" if z >= t else "N") 
  
  
  
if __name__ == "__main__":
  tc = 1
  
  for t in range(1, tc+1):
    p(solve())
