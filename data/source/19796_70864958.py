import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print



m, n = mii()
l = [mii() for _ in range(n)]

k = [0] * m

for a, b in l:
  for i in range(a, b + 1):
    k[i - 1] = 1

p("YES" if sum(k) == m else "NO")