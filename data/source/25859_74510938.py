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
  s = input()
  d = {}

  for i in s:
    d[i] = d.get(i, 0) + 1

  d = sorted(d.items(), key = lambda t:(-t[1], t[0]))

  for k, v in d:
    print(end=k * v)

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()