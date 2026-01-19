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
  k = mii()
  a = mii()
  b = mii()

  for i in range(n):
    l = sorted([k[i], a[i], b[i]])
    print(l[1], end = " ")

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    solve()