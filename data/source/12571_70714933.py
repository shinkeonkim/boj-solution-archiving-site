import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())

for _ in range(ii()):
  n = ii()
  l = sorted([mii() for i in range(n)])
  ans = 0
  if n == 2:
    ans += int(l[1][1] < l[0][1])
  
  print(f"Case #{_+1}: {ans}")