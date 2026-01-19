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
  n, t, t_0 = mii()
  for _ in range(n):
    m, *l = mii()
    cnt = 0
    sm = 0
    mx = 0
    
    for i in range(m):
      mx = max(mx, l[i])
      
      if sm + l[i] - (mx - t_0 if mx >= t_0 else 0) <= t:
        cnt += 1
        sm += l[i]
      else:
        break
    print(cnt)

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
    
