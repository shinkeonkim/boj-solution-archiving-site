import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,input().split(x))]
mfi = lambda x = " ": [*map(float,input().split(x))]
ii = lambda : int(input())

n = ii()
l = mii()
t = ii()

mn = 11111111111111111111
ans = 0

for i in l:
  if t % i < mn:
    mn = t % i
    ans = i
print(ans)