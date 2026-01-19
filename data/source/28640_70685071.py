import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,inp().split(x))]
mfi = lambda x = " ": [*map(float,inp().split(x))]
ii = lambda : int(inp())


a, b = map(len, input().split("|"))
c, d = map(len, input().split("|"))

print("Yes" if a == c or a == d or b == c or b == d else "No")