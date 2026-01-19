import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,input().split(x))]
mfi = lambda x = " ": [*map(float,input().split(x))]
ii = lambda : int(input())

l = mii()
idx = []
for i in range(10):
  if l[i] > 0:
    idx.append(i)
    
if (l[idx[1]] - l[idx[0]]) % (idx[1] - idx[0]) != 0:
  print(-1)
  sys.exit()

z = (l[idx[1]] - l[idx[0]]) // (idx[1] - idx[0])

s = l[idx[0]] - z * idx[0]

for i in range(10):
  print(s + i * z, end = " ")