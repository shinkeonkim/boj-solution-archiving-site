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
  n = ii()
  
  if n == 1:
    p(0)
    return
  
  points = [mii() + [i + 1] for i in range(n)]
  points.sort(key = lambda t: (t[0], t[1]))
  
  ans = []
  
  for i in range(0, n - 1, 2):
    ans.append([points[i][2], points[i+1][2]])
  
  p(len(ans))

  for i in ans:
    p(*i)
  
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()

