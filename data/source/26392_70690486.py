import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,inp().split(x))]
mfi = lambda x = " ": [*map(float,inp().split(x))]
ii = lambda : int(inp())

tc, r, c = mii()

for _ in range(tc):
  l = [input() for i in range(r)]
  
  d = []
  
  for j in range(c):
    for i in range(r):
      if l[i][j] == '#':
        d.append(i)
  print(max(d) - min(d))