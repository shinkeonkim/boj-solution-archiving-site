import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())

c = fi()
n = ii()
l = [mfi() for i in range(n)]

s = 0

for i in l:
  s += i[0] * i[1] * c

print(s)