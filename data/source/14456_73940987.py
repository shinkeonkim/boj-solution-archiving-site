import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta

BLANK = " "

#inp = input
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def f(a, l):
  ret = 0
  for i, j in l:
    X = a.index(i)
    Y = a.index(j)
    
    if (X == 0 and Y == 2) or (X - 1 == Y):
      ret += 1
  return ret


def solve():
  n = ii()
  l = [mii() for _ in range(n)]
  ans = 0
  
  k = [[1, 2, 3],[1 ,3, 2],[2, 1, 3],[2, 3, 1],[3, 1, 2],[3, 2, 1]]
  for i in k:
    ans = max(ans, f(i, l))
  
  p(ans)
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
    