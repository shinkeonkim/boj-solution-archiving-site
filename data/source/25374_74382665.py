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
  N = ii()
  
  scores = sorted(mii(), reverse = True)
  
  d = [3, 10, 22, 39, 59, 76, 88, 95, 99]
  
  ans = []
  
  for idx in d:
    standard = scores[idx]
    
    ans.append(len([i for i in scores if i >= standard]))
  
  prev = 0
  for i in ans:
    p(i - prev)
    prev = i

    
tc = 1

for t in range(1, tc+1):
  ret = solve()