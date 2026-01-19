import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,inp().split(x))]
mfi = lambda x = " ": [*map(float,inp().split(x))]
ii = lambda : int(inp())


a, b = mii()
c, d = mii()
x, y, z = mii()

k = x * y * z * (a * b + c * d)
print(k)