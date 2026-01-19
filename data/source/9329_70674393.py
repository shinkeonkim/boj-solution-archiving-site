import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,inp().split(x))]
mfi = lambda x = " ": [*map(float,inp().split(x))]
ii = lambda : int(inp())


for _ in range(ii()):
  n, m = mii()
  
  l = [mii() for i in range(n)]
  d = [0] + mii()
  
  ans = 0
  
  for i in range(n):
    k, *l2, cost = l[i]
    mn = min([d[i] for i in l2])
    ans += mn * cost
  print(ans)