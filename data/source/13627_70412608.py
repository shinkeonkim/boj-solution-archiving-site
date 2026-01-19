import sys
from math import sqrt
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,input().split(x))]
mfi = lambda x = " ": [*map(float,input().split(x))]
ii = lambda : int(input())

ans = []
n , r = mii()
l = sorted(mii())

crt = 1
for i in l:
  while i != crt:
    ans.append(crt)
    crt += 1
  crt += 1

for i in range(l[-1] + 1, n + 1):
  ans.append(i)

if len(ans) == 0:
  print("*")
else:
  print(*ans)