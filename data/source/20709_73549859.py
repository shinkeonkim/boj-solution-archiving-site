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
  l = [input().split() for _ in range(n)]
  
  idx = -1
  money = 11111111111111
  
  for i in range(n):
    m, v  = l[i]
    m = int(m)
    
    if v.count('2') > 1 and v.count('0') > 0 and v.count('1') > 0:
      if m < money:
        money = m
        idx = i
  p(idx + 1)

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()

