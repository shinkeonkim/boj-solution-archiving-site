import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,inp().split(x))]
mfi = lambda x = " ": [*map(float,inp().split(x))]
ii = lambda : int(inp())

def f(h, m, d):
  if h <= 1988:
    return 1
  
  if h >= 1990:
    return 0
  
  if m > 2:
    return 0
  
  if m == 1:
    return 1
  
  if d > 27:
    return 0
  
  return 1


l = [mii() for _ in range(ii())]

ans = 0
for h,m,d in l:
  print("Yes" if f(h, m, d) else "No")