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

def f(n, l):
  for i in range(n):
    if l[i].count("W") != l[i].count("B"):
      return False

  for i in range(n):
    d = 0
    for j in range(n):
      if l[j][i] == "W":
        d += 1
    if d * 2 != n:
      return False

  for i in range(n):
    for j in range(n - 2):
      if l[i][j] == l[i][j + 1] == l[i][j + 2]:
        return False

      if l[j][i] == l[j + 1][i] == l[j + 2][i]:
        return False

  return True

def solve():
  n = ii()

  l = [input() for _ in range(n)]

  p(1 if f(n, l) else 0)

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()