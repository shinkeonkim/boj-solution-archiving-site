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

INF = 999999999999999999999999999

def contains(num, l):
  num = str(num)
  for i in num:
    i = int(i)
    if i in l:
      return True
  return False

def solve():
  n, *l = mii()
  k = ii()
  
  ans = INF

  for i in range(1000):
    if contains(i, l):
      continue
    ans = min(ans, abs(k - i))
  p(ans)


if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
    
