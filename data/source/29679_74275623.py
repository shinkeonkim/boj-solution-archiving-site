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
  t, r, v = mfi()
  
  # 현재 위치 진행 
  # t초동안 진행
  # 현재 위치 측정
  
  # D : 도착 지점
  # S : 출발 지점
  # (D - S) = v * t
  
  S = 0
  D = v * t
  
  if 2 * r >= D:
    p(0)
  else:
    p((D - 2 * r) / t)
  
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
    
