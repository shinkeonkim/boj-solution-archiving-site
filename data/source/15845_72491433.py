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
  n, m = mii()
  problem = mii()
  
  ans = 0
  mx = 0
  
  for idx in range(n):
    l = mii()
    
    cnt = 0
    for i in range(m):
      if l[i] == problem[i]:
        cnt += 1
    
    if mx < cnt:
      mx = cnt
      ans = idx
  p(ans + 1)

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
        
