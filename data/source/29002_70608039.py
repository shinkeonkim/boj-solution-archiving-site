import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,input().split(x))]
mfi = lambda x = " ": [*map(float,input().split(x))]
ii = lambda : int(input())

n = ii()
l = mii()
k = sum(l) // 2

for i in l:
  if i == k:
    continue
  print(i, end = " ")
print(k)