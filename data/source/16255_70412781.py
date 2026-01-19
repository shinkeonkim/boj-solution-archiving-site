import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,input().split(x))]
mfi = lambda x = " ": [*map(float,input().split(x))]
ii = lambda : int(input())

for _ in range(ii()):
  k, x, y = mii()
  
  if x < y:
    x, y = y, x
  
  ans = max(0, k - x)
  x = max(x, k)
  
  while x - y < 2:
    x += 1
    ans += 1

  print(ans)