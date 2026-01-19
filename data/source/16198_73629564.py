import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta

BLANK = " "

inp = input
# inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def f(n, l, crt):
  if n == 2:
    return crt
  
  if n == 3:
    return crt + l[0] * l[2]
  
  mx = 0
  for i in range(1, n - 1):
    l2 = l[:i] + l[i+1:]
    k = f(n - 1, l2, crt + l[i - 1] * l[i + 1])
    
    mx = max(mx, k)
  
  return mx
  

def solve():
  n = ii()
  l = mii()

  k = f(n, l, 0)  
  
  p(k)
      

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()

