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


def solve():
  s = input()
  
  if "-" in s:
    s2 = s.replace("-", "")
    y = int(s[:2])
    
    if y <= 19:
      p("20"+s2)
    else:
      p("19"+s2)
  else:
    s2 = s.replace("+", "")
    y = int(s[:2])
    
    if y >= 40:
      p("18"+s2)
    else:
      p("19"+s2)
    
    
    
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
    
