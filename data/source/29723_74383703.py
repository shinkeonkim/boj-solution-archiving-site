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
  
  score = {}

  for i in range(n):
    a, b = inp().split()
    b = int(b)
    
    score[a] = b
  
  l = [inp() for _ in range(k)]
  
  ans = 0
  
  for i in l:
    ans += score[i]
    score[i] = -1
  
  s = sorted([i for i in score.values() if i != -1])
  
  left = m - k
  
  mn = sum(s[:left])
  
  s.reverse()
  
  mx = sum(s[:left])
  
  p(ans + mn, ans + mx)
  
  
tc = 1

for t in range(1, tc+1):
  ret = solve()