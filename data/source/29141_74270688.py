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

def gcd(a, b):
  return gcd(b, a % b) if b > 0 else a


def solve():
  start = mii()
  end = mii()
  
  a, b = mii() # 너비는 최소 a, 높이는 최대 b
  
  w = abs(start[0] - end[0])  
  h = abs(start[1] - end[1])
  
  if a > w:
    p(-1)
    return
  
  cnt = w // a
  
  if h > b * cnt:
    p(-1)
    return
  
  
  x, y = w, cnt
  g = gcd(x, y)
  p(x // g, y // g)
  
  x, h = h, cnt
  g = gcd(x, y)
  p(x // g, y // g)
      
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
    
