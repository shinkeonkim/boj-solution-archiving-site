import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,inp().split(x))]
mfi = lambda x = " ": [*map(float,inp().split(x))]
ii = lambda : int(inp())

n = ii()
l = mii()
ans = abs(l[1] - l[0])

for i in range(2, n):
  ans = min(ans, abs(l[i] - l[i - 1]))
print(ans)