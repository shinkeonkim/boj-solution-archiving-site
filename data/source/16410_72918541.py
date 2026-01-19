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

def dis(a, b):
  return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


def solve():
  x, y, x1, y1, x2, y2 = mii()
  
  l = [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]
  
  if x1 <= x <= x2:
    l.append((x, y1))
    l.append((x, y2))
  if y1 <= y <= y2:
    l.append((x1, y))
    l.append((x2, y))
  
  ans = 11111111111111111
  for i in l:
    d = dis((x, y), i)
    ans = min(ans, d)
  
  p(sqrt(ans))
    

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
