import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from decimal import Decimal
BLANK = " "

#inp = input
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  l = [input() for _ in range(8)]
  
  r = [1] * 8
  c = [1] * 8
  
  for i in range(8):
    for j in range(8):
      if l[i][j] == 'R':
        r[i] = 0
        c[j] = 0
  
  p(sum(r) * sum(c))
  
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
