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


def solve():
  N, K = mii()
  l = mii()
  cnt = 0
  
  for i in range(1, N):
    loc = i - 1
    new_item = l[i]
    
    while (0 <= loc and new_item < l[loc]):
      l[loc + 1] = l[loc]
      loc -= 1
      cnt += 1
      
      if cnt == K:
        p(*l)
        return
    
    if loc + 1 != i:
      l[loc + 1] = new_item
      cnt += 1
    if cnt == K:
      p(*l)
      return
  p(-1)
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
    