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
  n = ii()
  l = mfi()
  
  st_idx = -1
  for i in range(n):
    if 30 <= l[i] <= 30.2:
      st_idx = i 
      break
  
  if st_idx == -1:
    return 0
  
  k = l[st_idx + 3:]
  
  if len(k) == 0:
    return 0
  
  ans = min(k) - 30
  
  return ans
  
  
if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()
    
    p(f"Data Set {t}:")
    p(f"{ret:.2f}")
    p()
