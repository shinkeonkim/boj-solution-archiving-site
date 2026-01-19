import sys
from math import sqrt
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,input().split(x))]
mfi = lambda x = " ": [*map(float,input().split(x))]
ii = lambda : int(input())

n, k = mii()
l = mii()

crt = 0
ans = 0

for i in l:
  if i <= crt:
    crt -= i
  else:
    crt = k - i
    ans += 1
print(ans)