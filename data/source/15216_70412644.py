import sys
from math import sqrt
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,input().split(x))]
mfi = lambda x = " ": [*map(float,input().split(x))]
ii = lambda : int(input())

h, w, n = mii()
l = mii()

crt = 0
cnt = 0

for i in l:
  crt += i
  
  if crt > w:
    print("NO")
    break
  if crt == w:
    cnt += 1
    crt = 0
  if cnt >= h:
    print("YES")
    break