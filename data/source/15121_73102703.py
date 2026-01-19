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
  n = ii()

  ans = []
  for a in range(2, n):
    for b in range(a - 1, a + 1):
      if n % (a + b) == 0 or (n - a) % (a + b) == 0:
        ans.append((a, b))
  p(f"{n}:")
  for a, b in ans:
    p(f"{a},{b}")

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()