import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,inp().split(x))]
mfi = lambda x = " ": [*map(float,inp().split(x))]
ii = lambda : int(inp())


K, n = mii()
l = [mii() for i in range(K)]
ans = 0

for i in range(1, n + 1):
  for j in range(i + 1, n + 1):

    ret = set()
    for k in range(K):
      a = l[k].index(i)
      b = l[k].index(j)
      ret.add(int(a < b))

    if len(ret) == 1:
      ans += 1
print(ans)