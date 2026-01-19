import sys
from math import sqrt, pi, sin, factorial, ceil, floor

BLANK = " "

# inp = input
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  n, s, k = mii()
  l = mii()
  
  d = [0] * n
  
  for i in l:
    idx = (i - 1) // s
    d[idx] += 1
  
  sz = max(d)
  
  for i in range(sz, 0, -1):
    for j in range(n):
      if d[j] >= i:
        p(end="#")
      else:
        p(end=".")
    p()
  p("-" * n)
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
