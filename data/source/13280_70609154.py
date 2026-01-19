import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,inp().split(x))]
mfi = lambda x = " ": [*map(float,inp().split(x))]
ii = lambda : int(inp())

while 1:
  n = ii()
  if n == 0:
    break
  
  l = sorted(mii())
  ans = 111111111111111111
  for i in range(1, n):
    ans = min(ans, l[i] - l[i - 1])
  print(ans)