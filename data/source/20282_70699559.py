import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,inp().split(x))]
mfi = lambda x = " ": [*map(float,inp().split(x))]
ii = lambda : int(inp())


C = ii()
l = [ii() for _ in range(C)]
ans = 100
k = 100

for i in l:
  k += i

  ans = max(k, ans)
print(ans)