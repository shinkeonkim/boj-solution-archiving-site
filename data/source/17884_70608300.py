import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,input().split(x))]
mfi = lambda x = " ": [*map(float,input().split(x))]
ii = lambda : int(input())

n = ii()
if n == 1:
  print("1")
  sys.exit()
l = mii()

k = [[i, l[i]] for i in range(n - 1)]
k.sort(key = lambda t: t[1])

print(1, end = " ")
for i, _ in k:
  print(i + 2, end = " ")