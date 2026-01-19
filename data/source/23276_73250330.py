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


def gcd(a, b):
  return a if b == 0 else gcd(b, a % b)

def solve():
  ans = 111111111111
  for _ in range(ii()):
    y, a, b = mii()
    y += a * b // gcd(a, b)
    ans = min(ans, y)
  p(ans)
  
  

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
