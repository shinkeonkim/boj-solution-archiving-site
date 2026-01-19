import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  n, m = mii()
  l = [mii() for _ in range(n)]

  l.sort(key=lambda t : (-t[0], -t[1]))
  
  a = 0
  b = 1111111111111
  for i in range(min(n, m)):
    a += l[i][0]
    b = min(b, l[i][1])
  p(a, b)
  
  
if __name__ == "__main__":
  tc = 1
  
  for t in range(1, tc+1):
    solve()
