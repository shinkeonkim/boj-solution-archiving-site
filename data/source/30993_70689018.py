import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,inp().split(x))]
mfi = lambda x = " ": [*map(float,inp().split(x))]
ii = lambda : int(inp())

n, a, b, c = mii()

print(factorial(n) // (factorial(a) * factorial(b) * factorial(c)))
