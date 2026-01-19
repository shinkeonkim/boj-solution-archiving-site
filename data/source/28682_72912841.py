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
  n = ii()
  
  for i in range(n):
    p(end = "swimming ")
  p()
  
  sys.stdout.flush()

  chk = input().split()
    
  for j in chk:
    if j == "bowling":
      p(end = "soccer ")
    else:
      p(end = "bowling ")
  p()
  sys.stdout.flush()
    
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
    
