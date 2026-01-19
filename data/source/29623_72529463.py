import sys
from math import sqrt, pi, sin, factorial
from decimal import *

inp = input
# inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def solve():
  epsilon = sys.float_info.epsilon
  a,b,c,d = mii()
  a = Decimal(a)
  b = Decimal(b)
  c = Decimal(c)
  d = Decimal(d)
  
  x = a + b.sqrt()
  y = c + d.sqrt()

  if abs(x - y) <= epsilon:
    return "Equal"
  if x > y:
    return "Greater"
  return "Less"

if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    d = solve()
    p(d)