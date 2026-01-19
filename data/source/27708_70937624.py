import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  inp()
  n = ii()
  l = sorted(mii())
  
  i = 0
  j = n - 1

  p(n)
  while i <= j:
    if i == j:
      p(l[i], end = " ")
    else:
      p(l[i], l[j], end = " ")
    i += 1
    j -= 1
  p()
  
  
if __name__ == "__main__":
  tc = ii()
  p(tc)
  p()
  
  for t in range(1, tc+1):
    solve()
