import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,inp().split(x))]
mfi = lambda x = " ": [*map(float,inp().split(x))]
ii = lambda : int(inp())

for _ in range(ii()):
  n, *l = mii()
  
  cnt = {}
  
  for i in range(1, 2 * n, 2):
    cnt[l[i]] = cnt.get(l[i], 0) + 1
  print(max(cnt.values()))