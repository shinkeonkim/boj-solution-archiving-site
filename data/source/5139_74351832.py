import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta
sys.setrecursionlimit(10**7)

BLANK = " "

#inp = input
inp = lambda : sys.stdin.readline().rstrip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  ans = []
  
  r, c = mii()
  
  mp = [input() for _ in range(r)]
  
  for x in range(c):
    cost = 0
    for y in range(r):
      if mp[y][x] == 'X':
        ans.append(cost)
        break
      if mp[y][x] == 'H':
        cost += 3
      else:
        cost += 1
    else:
      ans.append('N')
  return ans

tc = ii()

for t in range(1, tc+1):
  ret = solve()
  p(f"Data Set {t}:")
  p(*ret)
  p()
    