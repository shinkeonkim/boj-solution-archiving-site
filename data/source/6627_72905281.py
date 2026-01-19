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

def f(n):
  return sum([*map(int, list(str(n)))])

def solve():
  while 1:
    n = ii()
    
    n2 = f(n)
    
    if n == 0:
      break
    
    for p in range(11, 1000):
      k = f(n * p)
      
      if n2 == k:
        print(p)
        break
    
    
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
    
