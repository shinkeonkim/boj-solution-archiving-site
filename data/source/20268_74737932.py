import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta
# sys.setrecursionlimit(10**7)

BLANK = " "

# inp = input
inp = lambda : sys.stdin.readline().rstrip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

  

def solve():
  n, m = mii()
  a = set(mii())
  b = set(mii())
  
  cnt = 0
  
  for i in range(16):
    A = set()
    B = set()
    if i & 1 > 0:
      A.add(0)
      B.add(0)
    if i & 2 > 0:
      A.add(0)
      B.add(1)
    if i & 4 > 0:
      A.add(1)
      B.add(0)
    if i & 8 > 0:
      A.add(1)
      B.add(1)
    
    
    if set(a) == A and set(b) == B:
      cnt += 1
  
  p(cnt)
  
if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()
