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
  n, a, b = input().split()
  n = int(n)
  
  same = 0
  similar = 0
  
  A = {}
  B = {}
  
  for i in range(n):
    if a[i] == b[i]:
      same += 1
    else:
      A[a[i]] = A.get(a[i], 0) + 1
      B[b[i]] = B.get(b[i], 0) + 1
  
  for k, v in B.items():
    v2 = A.get(k, 0)
    
    similar += min(v, v2)
  
  p(same, similar)
  
  
tc = 1

for t in range(1, tc+1):
  ret = solve()