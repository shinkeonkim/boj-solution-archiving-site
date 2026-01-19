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
  s = input()
  k = input()
  
  d = {}
  
  for i in range(26):
    d[s[i]] = i
  
  cnt = 1
  prev = d[k[0]]
  for i in range(1, len(k)):
    crt = d[k[i]]
    
    if prev >= crt:
      cnt += 1
    
    prev = crt
  
  p(cnt)
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
