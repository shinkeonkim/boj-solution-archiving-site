import sys
from math import sqrt, pi, sin, factorial, ceil, floor

BLANK = " "

inp = input
# inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  n = ii()
  tm = [0] * 1100
  mn = 111111111111111
  mx = 0
  for i in range(n):
    _, a, b = input().split()
    a = int(a)
    b = int(b)
    
    for j in range(a, b):
      tm[j] += 1
    
    mn = min(mn, a)
    mx = max(mx, b)
  
  for i in range(mn, mx):
    if tm[i] == 0:
      continue
    p(end=chr(64 + tm[i]))
  p()
    
  
if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()
        
