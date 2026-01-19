import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,input().split(x))]
mfi = lambda x = " ": [*map(float,input().split(x))]
ii = lambda : int(input())


for i in range(ii()):
  G, C, E = mii()
  
  cnt = 0
  while C < E:
    cnt += 1
    if G == 1:
      C += 1
    if G == 2 and cnt % 3 == 0:
      C += 1
    
    if G == 3 and cnt % 5 == 0:
      C += 1
  print(cnt)
