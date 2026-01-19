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

def f(a, b):
  return abs(a[0] - b[0]) <= 1 and abs(a[1] - b[1]) <= 1

def solve():
  fixed = mii()
  n = ii()

  crt = [0, 0]

  d = {
    "I": (1, 0),
    "S": (0, 1),
    "Z": (-1, 0),
    "J": (0, -1)
  }

  ans = []

  k = input()
  for idx in range(n):
    i = k[idx]
    if f(crt, fixed):
      ans.append(idx)
    diff = d[i]
    crt[0] += diff[0]
    crt[1] += diff[1]

  if f(crt, fixed):
    ans.append(n)

  if len(ans) == 0:
    p(-1)
  else:
    p(*ans, sep="\n")

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()