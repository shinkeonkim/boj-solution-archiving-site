import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from decimal import Decimal
BLANK = " "

#inp = input
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def solve():
  a, b = mfi()
  diff = b - a

  ans = []

  for i in [50, 20, 10, 5, 1]:
    c = int(diff // i)

    ans.append(c)
    diff -= c * i
  p("{}-$50, {}-$20, {}-$10, {}-$5, {}-$1".format(*ans))

if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()