import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())


def solve():
  L, n = mii()
  l = mii()
  
  cnt = 0
  while L != 0:
    L = l[L - 1]
    cnt += 1
  
  print(cnt)


if __name__ == "__main__":
  tc = ii()
  for t in range(tc):
    print(f"Data Set {t+1}:")
    solve()
    print()
    