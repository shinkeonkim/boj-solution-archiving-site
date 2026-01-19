import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,inp().split(x))]
mfi = lambda x = " ": [*map(float,inp().split(x))]
ii = lambda : int(inp())

l = [0] * 1100

for i in range(ii()):
  s, t, b = mii()
  
  for i in range(s, t + 1):
    l[i] += b

print(max(l))