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


def f(l):
  if 3 in l:
    return "None"
  
  if sum(l) >= 5 * len(l):
    return "Named"

  if sum(l) * 2 >= 9 * len(l):
    return "High"
  
  return "Common"

def solve():
  n = ii()
  
  l = [ii() for _ in range(n)]
  
  p(f(l))
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
    
