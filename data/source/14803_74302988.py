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
  D, N = mii() # D: 목적지, N: 도로에 있는 말의 수
  
  l = [mii() for _ in range(N)]
  
  mx_t = 0
  
  for loc, v in l:
    dis = D - loc
    t = dis / v
    
    mx_t = max(mx_t, t)
  
  return D / mx_t
  
  
if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()
    
    p(f"Case #{t}: {ret}")