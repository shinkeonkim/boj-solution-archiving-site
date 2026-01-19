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
  d = {}
  
  for _ in range(n):
    l = len(input().split())
    d[l] = d.get(l, 0) + 1
  
  d = sorted(d.items())
  
  for k, v in d:
    p(k, v)
  
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
   