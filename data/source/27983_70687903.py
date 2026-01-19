import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,inp().split(x))]
mfi = lambda x = " ": [*map(float,inp().split(x))]
ii = lambda : int(inp())


n = ii()
x = mii()
l = mii()
c = input().split()

for i in range(n):
  for j in range(1, n):
    if abs(x[i] - x[j]) <= l[i] + l[j] and c[i] != c[j]:
      print("YES")
      print(i + 1, j + 1)
      sys.exit()

print("NO")