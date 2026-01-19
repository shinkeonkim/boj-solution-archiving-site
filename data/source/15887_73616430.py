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
  l = mii()
  
  ans = []
  for i in range(1, n+1):
    idx = l.index(i)
    
    if idx == i - 1:
      continue
    
    k = i - 1
    
    ans.append([k+1, idx + 1])
    
    while k < idx:
      l[k], l[idx] = l[idx], l[k]
      k += 1
      idx -= 1
  
  p(len(ans))
  for i in ans:
    p(*i)

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()

