import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,inp().split(x))]
mfi = lambda x = " ": [*map(float,inp().split(x))]
ii = lambda : int(inp())


dx = [0,0,1,-1]
dy = [1,-1,0,0]

n,m = mii()
l = [mii() for i in range(n)]

for i in range(n):
  k = []
  for j in range(m):
    if i == 0 or j == 0 or i == n - 1 or j == m - 1:
      k.append(0)
      continue
    
    for d in range(4):
      v = l[i + dy[d]][j + dx[d]]
      if l[i][j] >= v:
        k.append(0)
        break
    else:
      k.append(1)
  print(*k)