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
  n = ii()
  a = input()
  
  m = ii()
  b = input()
  
  for i in b:
    if i not in a:
      p("-1")
      return
  
  idx = n - 1
  cnt = 0
  for i in range(m):
    crt = b[i]
    cnt += 1
    
    idx += 1
  
    while a[idx % n] != crt:
      idx += 1
      cnt += 1
  p(cnt)
    
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
