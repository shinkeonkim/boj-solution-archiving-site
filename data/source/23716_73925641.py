import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta

BLANK = " "

#inp = input
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def f(a, b):
  a = ord(a) - 97
  b = ord(b) - 97
  
  diff = abs(a - b)
  
  return min(diff, 26 - diff)


def solve():
  T = input()
  F = input()
  
  ans = 0
  for i in T:
    mn = 1111111111111111
    for j in F:
      cost = f(i, j)
      mn = min(mn, cost)
    
    ans += mn
  
  return ans
  
  
  
if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()
    
    p(f"Case #{t}: {ret}")