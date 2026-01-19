import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,inp().split(x))]
mfi = lambda x = " ": [*map(float,inp().split(x))]
ii = lambda : int(inp())


w, h = mii()
n, a, b = mii()

per_page = (w // a) * (h // b)

if per_page == 0:
  print(-1)
else:
  print(n // per_page + int(n % per_page > 0))