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
  n, m = input().split()
  n = int(n)
  M = float(m)
  
  # m, t, F
  l = [mfi() for _ in range(n)]
  
  for m, _, _ in l:
    M += m
  
  v = 0
  g = 9.81
  h = 0
  for i in range(n):
    m, t, F = l[i]
    
    a = F / M - g
    
    h += v * t + (1 / 2) * a * t * t
    v = v + a * t
    M -= m
  
  return f"{h:.2f}"
  
    
if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()
    
    p(f"Data Set {t}:")
    p(ret)
    p()
