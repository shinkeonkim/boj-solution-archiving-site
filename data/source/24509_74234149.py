import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta
sys.setrecursionlimit(10**7)

BLANK = " "

#inp = input
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  n = ii()
  l = [mii() for _ in range(n)]
  
  ans = []
  for sort_key in range(1, 5):
    l.sort(key = lambda t: (-t[sort_key], t[0]))
    
    for i in range(n):
      if l[i][0] in ans:
        continue
      
      ans.append(l[i][0])
      break
  p(*ans)
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
    
