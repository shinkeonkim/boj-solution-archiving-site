import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())


t = ii()
a, x = mii()
b, y = mii()

k = max((t - a) * x, 0) + max((t - a - b) * y, 0)
k2 = max((t - b) * y, 0) + max((t - a - b) * x, 0)

print(max(k, k2))