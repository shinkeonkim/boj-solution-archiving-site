import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,input().split(x))]
mfi = lambda x = " ": [*map(float,input().split(x))]
ii = lambda : int(input())

for _ in range(ii()):
  l = mii()
  ans = 0
  for i in range(1, len(l)):
    ans += max(0, l[i] - l[i - 1] * 2)
    
  print(ans)