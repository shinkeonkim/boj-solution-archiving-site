import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta

BLANK = " "

inp = input
# inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  n = ii()
  k = ii()
  l = [ii() for _ in range(k)]
  cnt = [0] * (n + 1)
  ans = 0
  
  sm = 0

  for i in l:
    for j in range(i, n + 1, i):
      cnt[j] = 1 - cnt[j]
      
      if cnt[j] == 1:
        sm += 1
      else:
        sm -= 1
      
    ans = max(ans, sm)
  p(ans)

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()

