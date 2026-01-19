import sys
from math import sqrt, pi, sin, factorial, ceil, floor

BLANK = " "

# inp = input
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  n = ii()
  a = b = 0
  for i in range(n):
    s = inp()
    
    a += s[:2].count('0')
    b += s[2:].count('0')
  
  ans = min(a//2, b//2)
  a, b = a - ans * 2, b - ans * 2
  p(ans, a, b)
  
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
