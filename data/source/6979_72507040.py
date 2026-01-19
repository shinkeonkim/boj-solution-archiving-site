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
  n = ii()
  a = mii()
  b = mii()
  
  mx = 0
  
  for i in range(n):
    for j in range(i + 1, n):
      if a[i] <= b[j]:
        mx = max(mx, abs(i - j))
  p(f"The maximum distance is {mx}\n")

if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()
   