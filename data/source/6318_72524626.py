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
  t = 0
  while 1:
    t += 1
    n = ii()
    if n == 0:
      break
    l = mii()
    
    k = sum(l) // n
    
    s = sum([abs(k - i) for i in l]) // 2
    
    p(f"Set #{t}")
    p(f"The minimum number of moves is {s}.")
    p()

  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
   