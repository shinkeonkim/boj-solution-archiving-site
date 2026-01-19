import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,inp().split(x))]
mfi = lambda x = " ": [*map(float,inp().split(x))]
ii = lambda : int(inp())

def f(a):
  if a < 0.2:
    return "weak"
  if a < 0.4:
    return "normal"
  if a < 0.6:
    return "strong"
  return "very strong"

p, r = mfi()
d = p / r

print(f(d))