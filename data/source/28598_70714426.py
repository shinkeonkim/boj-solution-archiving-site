import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())


x1, x2, n = mii()

d = x1 - x2

print("YES" if d % 2 == 0 and (d // 2) >= n else "NO")
