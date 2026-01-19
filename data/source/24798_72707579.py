import sys
from math import sqrt, pi, sin, factorial, ceil, floor

BLANK = " "

inp = input
# inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  l, w = mii()
  
  avg = w // l
  left = w % l
  ans = ""

  for i in range(l):
    z = avg
    if i < left:
      z += 1
    
    if z > 26 or z <= 0:
      p("impossible")
      return
    
    ans += chr(z + 96)
  p(ans)
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()