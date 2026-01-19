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
  h, k, v, s = mii()
  
  dis = 0
  while h > 0:
    v += s
    v -= max(1, int(v // 10))
    
    if v >= k:
      h += 1
    elif 0 < v < k:
      h -= 1
      
      if h == 0:
        v = 0
    else:
      h = v = 0
    
    dis += v
    
    if s > 0:
      s -= 1
  p(dis)

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
