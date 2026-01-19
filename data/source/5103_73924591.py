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


def solve():
  while 1:
    code = input()
    
    if code == '#':
      break

    mx, crt = mii()
    
    for _ in range(ii()):
      flag, val = input().split()
      val = int(val)
      
      if flag == 'S':
        crt = max(0, crt - val)
      else:
        crt = min(mx, crt + val)
    p(code, crt)
  
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
