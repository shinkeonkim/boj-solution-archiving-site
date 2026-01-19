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
  M, N = mii() # M: 코인수, N: 해적 수
  
  # M 개를 N개의 동일한 더미로 나누고, K개 남김
  cnt = [0] * N
  for i in range(N):
    cnt[i] += M % N
    cnt[i] += M // N
    
    M = M - (M % N) - M // N
  
  p(*cnt)
  p(M)
  
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
    