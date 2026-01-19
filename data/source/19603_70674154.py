import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,inp().split(x))]
mfi = lambda x = " ": [*map(float,inp().split(x))]
ii = lambda : int(inp())


p = ii()
n = ii()
r = ii()

crt = n
prev = n
ans = 0

while crt <= p:
  crt += prev * r
  prev *= r
  ans += 1
print(ans)