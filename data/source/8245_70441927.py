import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,input().split(x))]
mfi = lambda x = " ": [*map(float,input().split(x))]
ii = lambda : int(input())

n, m = mii()
l = [input() for i in range(n)]

for j in range(m):
  for i in range(n - 1, -1, -1):
    print(end = l[i][j])
  print()