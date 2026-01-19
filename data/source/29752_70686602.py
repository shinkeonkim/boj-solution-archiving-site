import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,inp().split(x))]
mfi = lambda x = " ": [*map(float,inp().split(x))]
ii = lambda : int(inp())

n = ii()
l = mii()
crt = 0
ans = 0

for i in l:
  if i > 0:
    crt += 1
  else:
    crt = 0
  ans = max(ans, crt)
print(ans)