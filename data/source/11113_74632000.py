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


def f(a, b):
  return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
  

def solve():
  n = ii()
  points = [mfi() for _ in range(n)]
  
  m = ii()
  
  for _ in range(m):
    k = ii()
    
    path = mii()
    
    dis = 0
    
    for i in range(1, k):
      dis += f(points[path[i - 1]], points[path[i]])
    
    p(round(dis))
  
    
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
    
