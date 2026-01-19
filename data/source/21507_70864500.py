import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

a, b, c, d = mii()

k = min(a, b) + min(c, d)

z = int(sqrt(k))

ans = 0
for i in range(max(z - 3, 0), z + 3):
  if i * i <= k:
    ans = i

print(ans)