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

def f(a, b, s):
  cnt = s // (a + b)
  
  ret = (a - b) * cnt
  
  left = s % (a + b)
  
  ret += min(left, a)
  ret -= max(0, left - a)
  
  return ret


def solve():
  # Nikky
  a = ii()
  b = ii()
  
  # Byron
  c = ii()
  d = ii()
   # s 단계
  
  s = ii()
  
  A = f(a, b, s)
  B = f(c, d, s)
  
  if A > B:
    p("Nikky")
  elif A < B:
    p("Byron")
  else:
    p("Tied")

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
    
