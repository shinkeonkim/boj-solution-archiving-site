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
  total_weight = 0
  total_apple_price = 0
  for _ in range(ii()):
    cat, *l = input().split()
    l = [*map(int, l)]

    if cat == "B":
      total_weight += 6000
      continue

    cnt = (l[0] // 12) * (l[1] // 12) * (l[2] // 12)

    total_weight += 1000 + cnt * 500
    total_apple_price += cnt * 4000

  p(total_weight)
  p(total_apple_price)

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()