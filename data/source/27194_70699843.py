import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,inp().split(x))]
mfi = lambda x = " ": [*map(float,inp().split(x))]
ii = lambda : int(inp())


n, T = mii()
m = ii()
x, y = mii()

k = (m / x + (n - m) / y)
k = int(k // 60 + int(k % 60 > 0) - T)

print(max(k, 0))
