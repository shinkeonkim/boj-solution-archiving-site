import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,inp().split(x))]
mfi = lambda x = " ": [*map(float,inp().split(x))]
ii = lambda : int(inp())

n = ii()
l = [inp() for i in range(n)]

for i in l:
  a = i.count("a")
  print(min(len(i) - a, a))