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
  m, n = mii()
  l = mii()
  
  ans = 0
  st = 0
  direction = 0
  
  for i in range(m):
    if l[i] == 2:
      st = i
      direction = 1
    
    if l[i] == 3:
      st = i
      direction = -1
  
  for _ in range(n):
    nxt = st + direction
    
    if nxt < 0 or nxt >= m:
      direction *= -1
      nxt = st + direction
    
    if l[nxt] == 0:
      ans += 1
    
    st = nxt
  p(ans)
    
if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()
    
