import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())


k = inp()
n = ii()
l = [input().split() for _ in range(n)]
s = {k}

for a, b in l:
  if k == b:
    k = a
    s.add(a)

print(k)
print(len(s))

