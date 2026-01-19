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


def f(a, b):
  for i in range(1, min(len(a), len(b)) + 1):
    suffix = a[-i:]
    prefix = b[:i]
    
    if suffix == prefix:
      return True
  return False
  

def solve():
  n = ii()
  names = [inp() for _ in range(n)]
  
  cnt = 0
  
  for i in range(n):
    for j in range(i + 1, n):
      if f(names[i], names[j]):
        cnt += 1
      elif f(names[j], names[i]):
        cnt += 1
  
  p(cnt)
  
  
tc = 1

for t in range(1, tc+1):
  ret = solve()