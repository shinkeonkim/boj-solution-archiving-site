import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta
# sys.setrecursionlimit(10**7)

BLANK = " "

# inp = input
inp = lambda : sys.stdin.readline().rstrip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

  
def solve():
  n, k, x, y = mii()
  # k의 배수인 층에 x개, 나머지는 y개
  # 전체 n 층
  
  ii()
  
  query = mii() # q개
  
  A = n // k
  B = n - A
  
  total = A * x + B * y
  
  unit = x + y * (k - 1)

  for q in query:
    q -= 1
    
    q %= total
    
    unit_cnt = q // unit
    unit_left = q % unit
    
    ans = unit_cnt * k
    
    if unit_left < unit - x:
      ans += unit_left // y
    else:
      ans += k - 1
    p(ans + 1)
    
    
    
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
