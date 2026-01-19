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
  l = []
  chk = [i for i in range(25000)]

  for i in range(2, 25000):
    if chk[i] == i:
      l.append(i)
      if i > 3:
        l.append(2 * i)
      for j in range(i + i, 25000, i):
        chk[j] = -1
  
  p(*l[:ii()])
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
    
