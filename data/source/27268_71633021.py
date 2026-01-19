import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  h, w, n = mii()
  l = [mii() for _ in range(n)]
  
  d = [[0] * w for _ in range(h)]
  
  for i in range(n):
    y, x, ey, ex = l[i]
    for k in range(y - 1, ey):
      d[k][x - 1] = i + 1
      d[k][ex - 1] = i + 1
      
    for k in range(x - 1, ex):
      d[y - 1][k] = i + 1
      d[ey - 1][k] = i + 1
  
  for i in d:
    for j in i:
      if j == 0:
        print(end=".")
      else:
        print(end=chr(96+j))
    print()

if __name__ == "__main__":
  tc = 1
  
  for t in range(1, tc+1):
    solve()
