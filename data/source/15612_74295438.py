import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta
sys.setrecursionlimit(10**7)

BLANK = " "

#inp = input
inp = lambda : sys.stdin.readline().rstrip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def f(n):
  l = []
  
  if n == 0:
    return 0

  while n > 0:
    l.append(n % 3)
    n //= 3
  
  return "".join([*map(str, l[::-1])])

def solve():
  n = ii()
  
  p(f(n))
  
  

if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()
