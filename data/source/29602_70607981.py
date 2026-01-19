import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,input().split(x))]
mfi = lambda x = " ": [*map(float,input().split(x))]
ii = lambda : int(input())


n = ii()
l = mii()
d = []
for i in range(n):
  d.append([l[i], 0, i])
  
d.sort(key = lambda t : t[0])

for i in range(n):
  d[i][1] = i + 1

d.sort(key = lambda t : t[2])

for _, i, _ in d:
  print(i, end = " ")