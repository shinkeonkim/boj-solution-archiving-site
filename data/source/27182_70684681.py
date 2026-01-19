import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,inp().split(x))]
mfi = lambda x = " ": [*map(float,inp().split(x))]
ii = lambda : int(inp())


now, pp = mii()

pp_2 = now - 14

if now - 7 > 0:
  print(now - 7)
else:
  print(pp + 7)
