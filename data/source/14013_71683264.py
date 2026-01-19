import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def solve():
  x, y = mfi()
  n = ii()

  for _ in range(n):
    z, q = inp().split()
    z = float(z)

    if q == 'A':
      p(z * y / x)
    else:
      p(z * x / y)

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    solve()