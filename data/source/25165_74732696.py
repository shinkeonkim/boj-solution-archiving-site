import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta
sys.setrecursionlimit(10**7)

BLANK = " "

# inp = input
inp = lambda : sys.stdin.readline().rstrip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

  
def solve():
  n, m = mii()
  start_c, D = mii() # D = 0: left
  r, c = mii()
  
  if r == 1:
    if (c < start_c and D == 0) or (c > start_c and D == 1):
      return True
  elif r <= n - 1:
    return True
  else:
    return (n + D) % 2 == 0
  
  
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()

    if ret:
      p("NO...")
    else:
      p("YES!")
      
