import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,inp().split(x))]
mfi = lambda x = " ": [*map(float,inp().split(x))]
ii = lambda : int(inp())


a, b, c = mfi()

x = 2 * a * 229 * 324 / 1000000
y = 2 * b * 297 * 420 / 1000000
z = c * 210 * 297 / 1000000
print(x + y + z)