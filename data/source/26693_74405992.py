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
  n, k = mii()
  l = mii()
  
  d = {}
  
  for i in l:
    d[i] = d.get(i, 0) + 1
    
  l = sorted(d.items(), key = lambda t:-t[0])
  
  sm = 0
  idx = 0
  while sm < k:
    sm += l[idx][1]
    idx += 1
  
  p(sm)
  
  

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
