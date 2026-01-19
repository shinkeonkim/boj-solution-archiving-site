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
  n, s = mii()
  
  crt = s
  cnt = 0

  for i in range(n):
    query = input()
    
    if query[-1] == 'L':
      # 라떼
      quantity = int(query[:-1]) + 1
    else:
      #에스프레소
      quantity = int(query)
    
    if crt >= quantity:
      crt -= quantity
    else:
      cnt += 1
      crt = s - quantity
  p(cnt)
      
      
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
