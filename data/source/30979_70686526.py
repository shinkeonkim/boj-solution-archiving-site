import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,inp().split(x))]
mfi = lambda x = " ": [*map(float,inp().split(x))]
ii = lambda : int(inp())


t = ii()
inp()
s = sum(mii())

print("Padaeng_i", "Happy" if t <= s else "Cry")
