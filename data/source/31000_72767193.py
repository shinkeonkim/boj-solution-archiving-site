import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from decimal import Decimal
BLANK = " "

inp = input
# inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  n = ii()
  cnt = 0
  
  for i in range(-n, n+1):
    if i == 0:
      continue
    for j in range(-n, n + 1):
      mn = i + j - n
      mx = i + j + n
      
      if mn <= 1 <= mx:
        cnt += 1
        
  cnt += (2 * n + 1) ** 2 # 
  p(cnt)
  

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()