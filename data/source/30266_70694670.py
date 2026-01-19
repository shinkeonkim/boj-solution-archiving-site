import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,inp().split(x))]
mfi = lambda x = " ": [*map(float,inp().split(x))]
ii = lambda : int(inp())

for _ in range(ii()):
  n = ii()
  k = inp().strip()
  l = [inp().strip() for i in range(n)]
  print(f"Data Set {_+1}:")
  cnt = 0
  for i in l:  
    for j in k:
      if j in i:
        cnt += 1
        break
  print(cnt)
  print()