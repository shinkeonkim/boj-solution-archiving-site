import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,inp().split(x))]
mfi = lambda x = " ": [*map(float,inp().split(x))]
ii = lambda : int(inp())


n = ii()
l = [mii() for i in range(n)]

mx_idx = 0

for i in range(n):
  if l[i][1] > l[mx_idx][1]:
    mx_idx = i

if l[mx_idx][1] == 0:
  print(0)
else:
  print(l[mx_idx][0] + mx_idx * 20)