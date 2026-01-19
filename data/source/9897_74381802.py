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
  L, G, R = mii()
  # 램프 수, 경비원 수, 총 순찰 횟수
  
  guards = [inp().split() for _ in range(G)]
  
  plans = [inp() for _ in range(R)]
  
  lamp = [0] * (L + 1)
  
  guard_idx = {}
  
  for i in range(G):
    guard_idx[guards[i][0]] = i
  
  for plan_name in plans:
    guard = guards[guard_idx[plan_name]]
    
    idx = int(guard[1])
    step = int(guard[2])
  
    while idx <= L:
      lamp[idx] = 1 - lamp[idx]
      
      idx += step
    
  p(sum(lamp))
  
  
tc = 1

for t in range(1, tc+1):
  ret = solve()