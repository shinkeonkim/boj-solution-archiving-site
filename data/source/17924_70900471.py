import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

n = ii()
l = [mii() for _ in range(n)]

s, e = -1, 1110000

for a, b in l:
  if b < s or e < a:
    print("edward is right")
    break

  s, e = max(s, a), min(e, b)
else:
  print("gunilla has a point")