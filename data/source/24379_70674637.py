import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,inp().split(x))]
mfi = lambda x = " ": [*map(float,inp().split(x))]
ii = lambda : int(inp())


A = mii()
B = mii()
money = ii()

l = [[A[i], B[i]] for i in range(3)]
l.sort(key = lambda t: t[0])

ans = 0

for price, cnt in l:
  if price == 0:
    ans += cnt
    continue
  buy = min(money // price, cnt)
  ans += buy
  
  money -= buy * price 
print(ans)