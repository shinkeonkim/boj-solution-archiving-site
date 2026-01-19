import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from decimal import Decimal
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

  l = [1, 1]

  for i in range(17):
    l.append(l[-1] + l[-2])

  s = [1, 2]

  for i in range(2, len(l)):
    s.append(s[-1] + l[i])

  for i in range(len(s)):
    if s[i] >= n:
      p(i + 1)
      break

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()