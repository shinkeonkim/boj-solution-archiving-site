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

def dis(a, b):
  return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

def solve():
  n = ii()
  crt, *l = [mii() for _ in range(n)]
  
  mn = 1111111111111111111
  idx = 0
  
  for i in range(n - 1):
    d = dis(crt, l[i])
    
    if d < mn:
      mn = d
      idx = i
  
  p(*crt)
  p(*l[idx])
  p(f"{sqrt(mn):.2f}")
  
  
  
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
   