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
    gold = {}
    total = {}

    n = ii()

    if n == 0:
      break

    l = [input().split() for _ in range(n)]

    for year, _, tier in l:
      year = int(year)

      if tier == "Gold":
        gold[year] = gold.get(year, 0) + 1

      total[year] = total.get(year, 0) + 1

    gold = sorted(gold.items(), key = lambda t:(-t[1], t[0]))
    total = sorted(total.items(), key = lambda t:(-t[1], t[0]))

    p(gold[0][0], total[0][0])

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()