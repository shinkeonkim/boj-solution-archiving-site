import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,inp().split(x))]
mfi = lambda x = " ": [*map(float,inp().split(x))]
ii = lambda : int(inp())


x, n = map(int, input().split())
d = "1"
cnt = 1
while len(d) < n:
  cnt *= x
  d += str(cnt)
print(d[n - 1])