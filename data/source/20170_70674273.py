import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,inp().split(x))]
mfi = lambda x = " ": [*map(float,inp().split(x))]
ii = lambda : int(inp())


def gcd(a, b):
  return gcd(b, a % b) if b else a

a = mii()
b = mii()

A = B = 0

for i in a:
  for j in b:
    if i > j:
      A += 1
    if i < j:
      B += 1
      
d = gcd(A, 36)
print(A // d, "/", 36 // d, sep="")