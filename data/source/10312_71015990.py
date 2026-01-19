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
  
  z = 1
  while z <= n:
    z *= 3
  
  z //= 3
  
  while z > 0:
    if n >= z:
      print(n // z, end = " ")
      n = n - (n // z) * z
    else:
      print(0, end = " ")
    z //= 3
  p()

if __name__ == "__main__":
  tc = ii()
  
  for t in range(1, tc+1):
    d = solve()
