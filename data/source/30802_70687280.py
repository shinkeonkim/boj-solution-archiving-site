import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,inp().split(x))]
mfi = lambda x = " ": [*map(float,inp().split(x))]
ii = lambda : int(inp())


n = ii()
l = mii()
t, p = mii()

ans = 0
for i in l:
  ans += i // t + int(i % t > 0)

print(ans)
print(n // p, n % p)