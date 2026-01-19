import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,inp().split(x))]
mfi = lambda x = " ": [*map(float,inp().split(x))]
ii = lambda : int(inp())

n = ii()
l = [ii() for i in range(n)]

crt = l[0]
ans = 0

for i in range(1, n):
  if crt < l[i]:
    ans += l[i] - crt
  crt = min(crt, l[i])
print(ans)