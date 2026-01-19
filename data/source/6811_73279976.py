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

def solve():
  a = ii()
  b = ii()
  c = ii()

  total = ii()
  cnt = 0
  for i in range(total // a + 1):
    for j in range(total // b + 1):
      for k in range(total // c + 1):
        crt = a * i + b * j + c * k

        if crt == 0:
          continue

        if crt <= total:
          cnt += 1
          p(f"{i} Brown Trout, {j} Northern Pike, {k} Yellow Pickerel")

  p(f"Number of ways to catch fish: {cnt}")

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()