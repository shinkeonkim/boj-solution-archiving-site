import sys
from math import sqrt, pi, sin, factorial, ceil, floor

BLANK = " "

inp = input
# inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  n = ii()
  l = [ii() for _ in range(n)]
  
  cnt = {}
  for i in l:
    cnt[i] = cnt.get(i, 0) + 1
  
  mx = max(cnt.values())
  
  mn = 111111111111
  for k, v in cnt.items():
    if v != mx:
      continue
    
    mn = min(mn, k)
  p(mn)
  
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    if t != 1:
      input()
    ret = solve()
   