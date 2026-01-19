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
  v = ii()

  h = 1
  ans = 1e30

  while h * h <= v:
    y = 1

    while y * y <= v:
      if v % (h * y) == 0:
        x = v // (h * y)

        ans = min(ans, 2 * (h * y + h * x + x * y))

      y += 1

    h += 1
  prt(ans)


if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()

