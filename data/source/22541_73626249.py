import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta

BLANK = " "

# inp = input
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  while 1:
    n = ii()
    
    if n == 0:
      break
    cnt = 0
    for a in range(1, n):
      # b^2 + b = k
      
      k = 2 * n - a + a * a
      b = a + 1
      while b < n and b * b + b <= k:
        if b * b + b == k:
          cnt += 1
        b += 1
    p(cnt)

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()

