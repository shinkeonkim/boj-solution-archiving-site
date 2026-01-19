import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,input().split(x))]
mfi = lambda x = " ": [*map(float,input().split(x))]
ii = lambda : int(input())

ans = 0

for i in range(ii()):
  d, w = mii()
  
  th = d * pi / 180
  
  ans += sin(th) * w

print("{:.2f}".format(ans))