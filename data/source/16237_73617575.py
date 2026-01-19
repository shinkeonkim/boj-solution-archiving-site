import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta

BLANK = " "

inp = input
# inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  A, B, C, D, E = mii()
  ans = 0
  
  ans += E
  
  ans += D
  A = max(0, A - D)
  
  ans += C
  k = min(C, B) # 3과 2을 같이 사용한 횟수
  C -= k
  B -= k
  
  A = max(0, A - C * 2)
  
  k2 = B // 2
  ans += k2
  A = max(0, A - k2)
  
  k3 = B % 2
  if k3 == 1:
    ans += 1
    A = max(0, A - 3)
  
  ans += A // 5
  ans += int(A % 5 > 0)
  
  p(ans)
  

    
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()

