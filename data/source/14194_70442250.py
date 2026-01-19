import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,input().split(x))]
mfi = lambda x = " ": [*map(float,input().split(x))]
ii = lambda : int(input())

for _ in range(ii()):
  n = int(input())
  l = mii()
  k = (max(l) +min(l)) / 2
  
  k2 = sum(l) / n
  
  print("Yes" if abs(k - k2) < 1 else "No")