import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())

def solve():
  while 1:
    n, d = mii()

    if n == d == 0:
      break
    l = [mii() for _ in range(d)]
    for i in range(1, d):
      for j in range(n):
        l[0][j] &= l[i][j]

    print("yes" if sum(l[0]) > 0 else "no")
  
if __name__ == "__main__":
  tc = 1
  
  for t in range(tc):
    solve()
    