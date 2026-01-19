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
  n, w = mii()
  l = mii() # n개
  
  ans = []
  
  crt = 0
  for i in range(w):
    crt += l[i]
  
  ans.append(crt)
  
  for i in range(w, n):
    crt += l[i]
    crt -= l[i - w]
    
    ans.append(crt)
    
  ans = [int(i / w) for i in ans]
  return max(ans) - min(ans)
  
  
if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()
    
    p(f"Data Set {t}:")
    p(ret)
    p()
    