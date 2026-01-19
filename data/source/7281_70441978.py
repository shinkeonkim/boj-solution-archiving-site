import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,input().split(x))]
mfi = lambda x = " ": [*map(float,input().split(x))]
ii = lambda : int(input())

n = ii()
l = [mii() for i in range(n)]

crt = l[0][0]
ans = 0

for i in range(0, n):
  if l[i][1] == 0:
    continue
  
  ans = max(ans, l[i][0] - crt)
  crt = l[i][0]

print(ans)