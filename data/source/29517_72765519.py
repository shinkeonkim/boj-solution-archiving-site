import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from decimal import Decimal
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
  
  a = []
  b = []
  
  i = 2
  
  while i <= n:
    a.append(i)
    i *= 2
  
  i = 1
  
  while i <= n:
    b.append(i)
    i *= 3
  
  cnt = 0
  
  for i in a:
    for j in b:
      if i * j <= n:
        cnt += 1
      else:
        continue
  p(cnt)
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()