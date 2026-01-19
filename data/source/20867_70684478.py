import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,inp().split(x))]
mfi = lambda x = " ": [*map(float,inp().split(x))]
ii = lambda : int(inp())


m, s, g = mii()
a, b = mfi()
l, r = mii()

k1 = l / a + m / g
k2 = r / b + m / s

print("friskus" if k1 < k2 else "latmask")