import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,input().split(x))]
mfi = lambda x = " ": [*map(float,input().split(x))]
ii = lambda : int(input())

n = ii()
A = sorted(mii())
B = sorted(mii())

for i in range(n):
  if A[i] > B[i]:
    print("NE")
    break
else:
  print("DA")