import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,inp().split(x))]
mfi = lambda x = " ": [*map(float,inp().split(x))]
ii = lambda : int(inp())


n = ii()
s = inp()
k = ii()

if s == "annyong":
  if k % 2:
    print(k)
  else:
    print(k + 1 if k + 1 <= n else k - 1)
else:
  if k % 2:
    print(k + 1 if k + 1 <= n else k - 1)
  else:
    print(k)