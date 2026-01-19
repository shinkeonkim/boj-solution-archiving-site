import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta
sys.setrecursionlimit(10**7)

BLANK = " "

#inp = input
inp = lambda : sys.stdin.readline().rstrip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  n = ii()
  
  price = [ii() for _ in range(n - 1)]
  
  stations = [inp() for _ in range(n)]
  
  start = inp()
  des = inp()
  
  for i in range(n):
    if stations[i] == start:
      start = i
    if stations[i] == des:
      des = i
  
  dis = abs(start - des)
  
  return price[dis - 1]
  
if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()
    
    p(f"Data Set {t}:")
    p(ret)
    p()