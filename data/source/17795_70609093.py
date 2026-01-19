import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,inp().split(x))]
mfi = lambda x = " ": [*map(float,inp().split(x))]
ii = lambda : int(inp())

n = input()
a = n[0] + "0" * (len(n) - 1)
b = str(int(n[0]) + 1) + "0" * (len(n) - 1)

if abs(int(a) - int(n)) < abs(int(b) - int(n)):
  print(a)
else:
  print(b)