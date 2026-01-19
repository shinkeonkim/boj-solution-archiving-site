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

INF = 100000000000000000000000000000000000

def solve():
  X = [-INF, INF]
  Y = [-INF, INF]
  
  for _ in range(ii()):
    x, y, cat = input().split()
    x = int(x)
    y = int(y)
    
    if cat == 'L':
      X[1] = min(X[1], x - 1)
    
    if cat == 'R':
      X[0] = max(X[0], x + 1)
    
    if cat == 'D':
      Y[1] = min(Y[1], y - 1)

    if cat == 'U':
      Y[0] = max(Y[0], y + 1)
  
  d = (X[1] - X[0] + 1) * (Y[1] - Y[0] + 1)
  
  if INF == X[1] or -INF == X[0] or INF == Y[1] or -INF == Y[0]:
    p("Infinity")
  else:
    p(d)
    
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
