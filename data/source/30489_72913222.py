import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from decimal import Decimal
BLANK = " "

# inp = input
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  n, m, k = mii()
  l = sorted(mii(), reverse=True)
  
  ans = sum(l[:m])
  
  for i in range(m, min(m + k, n)):
    ans += l[i]
  
  p(ans * 100 / sum(l))
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
    
