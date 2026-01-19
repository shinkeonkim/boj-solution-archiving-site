import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from decimal import Decimal
BLANK = " "

inp = input
# inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def solve():
  N, H, W = mii()
  l = mii()

  d = [0] * (N * W)

  for i in range(N):
    if i % 2 == 1:
      start = W * i - l[i]
      for j in range(start, start + W):
        d[j] = i + 1
    else:
      ed = W * (i + 1) + l[i]
      for j in range(ed - W, ed):
        d[j] = i + 1

  p(d.count(0) * H)

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()