import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,inp().split(x))]
mfi = lambda x = " ": [*map(float,inp().split(x))]
ii = lambda : int(inp())


def f(n):
  d = [i * i for i in range(10, 200, 20)]

  for i in range(len(d)):
    if n <= d[i]:
      return 10 - i
  return 0

ans = 0
for i in range(ii()):
  a, b = mii()
  ans += f(a * a + b * b)

print(ans)