import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,input().split(x))]
mfi = lambda x = " ": [*map(float,input().split(x))]
ii = lambda : int(input())

n = ii()
l = sorted(mii())
ans = []

for i in range(0, n, 2):
  if i + 1 < n:
    ans.append(l[i + 1])
  ans.append(l[i])
print(*ans)