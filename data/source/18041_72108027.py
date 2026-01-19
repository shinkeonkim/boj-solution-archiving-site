import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  n, x = mii()
  
  l = mii()
  ans = 1
  crt = 1
  for i in range(1, n):
    if l[i] - l[i - 1] <= x:
      crt += 1
    else:
      crt = 1
    ans = max(ans, crt)
  
  p(ans)
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
