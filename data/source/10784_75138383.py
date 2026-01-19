import sys
from math import sqrt, pi, sin, cos, factorial, ceil, floor
from datetime import datetime, timedelta
# sys.setrecursionlimit(10**7)

BLANK = " "

# inp = input
inp = lambda : sys.stdin.readline().rstrip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
prt = print
def gcd(a, b): return gcd(b, a % b) if b > 0 else a
def lcm(a, b): return a * b // gcd(a, b)


def solve():
  p, a, b, c, d, n = mii()

  price = lambda k : p * (sin(a * k + b) + cos(c * k + d) + 2)

  mx = price(1)
  ans = 0

  for i in range(2, n + 1):
    crt = price(i)

    ans = max(ans, mx - crt)
    mx = max(mx, crt)
  
  prt(ans)
  

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()