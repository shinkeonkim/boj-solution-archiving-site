import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta
sys.setrecursionlimit(10**7)

BLANK = " "

# inp = input
inp = lambda : sys.stdin.readline().rstrip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  n, m, k = mii()
  # 농장의 층수, 비오는 횟수, 각 층이 버티는 빗물의 양
  
  l = [mii() for _ in range(m)] # 비의 정보 (t_i, r_i)
  # 1층부터 t_i 층까지 r_i만큼 받게 된다.
  
  s = 0
  for idx in range(m):
    _, r = l[idx]
    
    s += r
    
    if s > k:
      p(idx + 1, 1)
      break
  else:
    p(-1)
  
  
  
tc = 1

for t in range(1, tc+1):
  ret = solve()