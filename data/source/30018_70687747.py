import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,inp().split(x))]
mfi = lambda x = " ": [*map(float,inp().split(x))]
ii = lambda : int(inp())


n = ii()
a = mii()
b = mii()

ans = 0
for i in range(n):
  ans += abs(a[i] - b[i])
print(ans // 2)