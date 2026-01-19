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
  a = input().split()
  b = input().split()
  
  s = set()
  
  for i in range(n):
    if a[i] == b[i]:
      return "bad"
    
    k = sorted([a[i], b[i]])
    
    s.add(k[0] + " " + k[1])
  
  if len(s) == n // 2 and n % 2 == 0:
    return "good"
  
  return "bad"

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
    p(ret)
