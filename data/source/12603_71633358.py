import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  c = ii()
  n = ii()
  
  l = mii()
  
  for i in range(n):
    for j in range(i + 1, n):
      if c == l[i] + l[j]:
        print(i + 1, j + 1)
        return


if __name__ == "__main__":
  tc = ii()
  
  for t in range(1, tc+1):
    p(end=f"Case #{t}: ")
    solve()
