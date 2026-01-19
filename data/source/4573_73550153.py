import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta

BLANK = " "

# inp = input
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print
  

def solve():
  tc = 1
  while 1:
    n = ii()
    
    if n == 0:
      break
    
    l = [mii() for _ in range(n)]

    mx = 0
    idx = 0
    for i in range(n):
      diameter, price = l[i]
      
      j = diameter ** 2 /price
      
      if j > mx:
        mx = j
        idx = i
    p(f"Menu {tc}: {l[idx][0]}")
    tc += 1
      
      
      
      
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()

