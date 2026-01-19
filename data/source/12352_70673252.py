import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,inp().split(x))]
mfi = lambda x = " ": [*map(float,inp().split(x))]
ii = lambda : int(inp())


for _ in range(ii()):
  n = ii()
  l = mfi()
  for i in range(1, n - 1):
    if l[i] <= (l[i-1] + l[i+1]) / 2:
      continue
    l[i] = (l[i-1] + l[i+1]) / 2
  print(f"Case #{_+1}: {l[n - 2]}")