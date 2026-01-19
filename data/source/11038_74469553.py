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
  while 1:
    m, nmin, nmax = mii()
    
    if m == nmin == nmax == 0:
      break
    
    l = [ii() for _ in range(m)]
    
    d = {}
    
    for i in l:
      d[i] = d.get(i, 0) + 1
    
    d = sorted(d.items(), key = lambda t : (-t[0]))
    
    cnt = 0
    ans = 0
    mx = 0
    
    for i in range(len(d) - 1):
      k, v = d[i]
      cnt += v
      
      diff = k - d[i + 1][0] 
      
      if mx <= diff and nmin <= cnt <= nmax:
        mx = diff
        ans = cnt
      
      prev = k
    p(ans)
    
    
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
    
