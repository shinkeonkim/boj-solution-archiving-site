import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta
sys.setrecursionlimit(10**7)

BLANK = " "

# inp = input
inp = lambda : sys.stdin.readline().rstrip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

  
def solve():
  n = ii()
  s = [100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 500000, 1000000]
  
  l = [ii() for _ in range(n)]
  
  sm = 0
  for i in l:
    s[i - 1] = 0
  
  num = ii()

  if sum(s) >= num * (10 - n):
    p("no deal")
  else:
    p("deal")
    
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()

    
