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
  n, m = mii()
  
  l = [mii() for _ in range(n)]
  
  s = {*[i for i in range(1, n)]}
  
  for i in range(m):
    if l[0][i] == 0:
      continue
    k = {*[j for j in range(1, n) if l[j][i] == 100]}
    
    s = s.intersection(k)
  
  p(1, len(s) + 1)
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
