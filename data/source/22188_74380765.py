import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta
sys.setrecursionlimit(10**7)

BLANK = " "

#inp = input
inp = lambda : sys.stdin.readline().rstrip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  n, m = mii()
  # n : 가입자의 관세 수?, m : 발신 전화 수
  
  l = [mii() for _ in range(n)] # c, t, p
  d = mii() # 통화 시간

  prices = []
  
  for c, t, pr in l:
    price = c * 100
    for i in d:
      if i >= t:      
        t2 = i // t + int(i % t > 0)
        price += t2 * pr
    prices.append(price)
  
  mn = min(prices)
  
  for i in range(n):
    if prices[i] == mn:
      p(i + 1)
      break
  
  
tc = 1

for t in range(1, tc+1):
  ret = solve()