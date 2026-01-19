import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,inp().split(x))]
mfi = lambda x = " ": [*map(float,inp().split(x))]
ii = lambda : int(inp())


def f(a, b):
  return a + 10 * b

a, b = mii()
k = f(a, b)
ans = 0

for _ in range(5):
  a, b = mii()
  k2 = f(a, b)
  ans = max(ans, k2 + 1 - k)
print(ans)