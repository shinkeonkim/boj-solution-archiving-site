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
  while 1:
    l = []

    a, b = mfi()

    if a == b == -1:
      break

    l.append([a, b])

    while 1:
      a, b = mfi()

      if a == b == 0:
        break

      l.append([a, b])

    dis = 0
    fuel = 0
    for i in range(len(l) - 1):
      fir = l[i]
      sec = l[i+1]

      if fir[1] < sec[1]:
        continue

      dis += sec[0] - fir[0]
      fuel += fir[1] - sec[1]

    p(round(l[-1][1] * dis / fuel))

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()