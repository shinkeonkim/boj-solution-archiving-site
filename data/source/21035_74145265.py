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
  n, m = mii()
  l = [mii() for _ in range(n)]

  q = ii()

  row = {}
  col = {}

  for _ in range(q):
    cat, idx, val = input().split()
    idx = int(idx) - 1
    val = int(val)

    if cat == "row":
      row[idx] = row.get(idx, 0) + val
    else:
      col[idx] = col.get(idx, 0) + val

  sm = 0
  mn = 111111111111111111111
  mx = -111111111111111111111
  for i in range(n):
    for j in range(m):
      l[i][j] += row.get(i, 0) + col.get(j, 0)

      sm += l[i][j]
      mn = min(mn, l[i][j])
      mx = max(mx, l[i][j])

  p(sm, mn, mx)

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()