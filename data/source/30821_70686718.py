import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,inp().split(x))]
mfi = lambda x = " ": [*map(float,inp().split(x))]
ii = lambda : int(inp())


n = ii()

k = 1
for i in range(5):
  k *= n - i

for i in range(1, 6):
  k //= i
print(k)