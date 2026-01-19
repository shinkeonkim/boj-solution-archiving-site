import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,input().split(x))]
mfi = lambda x = " ": [*map(float,input().split(x))]
ii = lambda : int(input())

crt = 0
mx = 0
N, K = mii()

for i in range(N):
  a, b = mii()
  crt += (a - b)
  mx = max(mx, crt - K)

print(mx)