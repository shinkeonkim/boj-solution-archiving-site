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
  price = [ii() for _ in range(n)]
  standard = [ii() for _ in range(m)]
  
  cnt = [0] * n
  for st in standard:
    for i in range(n):
      if price[i] <= st:
        cnt[i] += 1
        break
  
  p(cnt.index(max(cnt)) + 1)
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
   