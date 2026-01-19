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
  while 1:
    n = ii()
    
    if n == 0:
      break
    mx = 0
    for i in range(0, 60):
      A = i ** 3
      
      if A > n:
        break
      for j in range(0, 1000):
        B = j * (j + 1) * (j + 2) // 6
        
        if A + B > n:
          break
        mx = max(A + B, mx)
    p(mx)
        
    
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
