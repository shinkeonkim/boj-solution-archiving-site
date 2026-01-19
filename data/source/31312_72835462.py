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
  n, a, b = mii()

  l = [ii() for _ in range(n - 1)]

  mn = min(l)
  mx = max(l)

  if (mn < a or mx > b) or (mn != a and mx != b):
    p(-1)
  elif mn == a and mx == b:
    for i in range(a, b + 1):
      p(i)
  elif mn != a:
    p(a)
  else:
    p(b)
  
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
    
