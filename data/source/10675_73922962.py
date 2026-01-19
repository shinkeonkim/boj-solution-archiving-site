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
  A, B, N = mii()
  
  # A -> B
  INF = 11111111111111111111111
  mn = INF
  
  chk = [A, B]
  
  for i in range(N):
    cost, k = mii()
    l = mii()
    
    idx = 0
    for j in l:
      if chk[idx] == j:
        idx += 1
      
      if idx == 2:
        mn = min(mn, cost)
        break
  p(-1 if mn == INF else mn)
    
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
