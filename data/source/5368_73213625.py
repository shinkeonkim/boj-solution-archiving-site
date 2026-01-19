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

def dis(a, b):
  return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

def solve():
  n = ii()
  l = [input() for _ in range(n)]

  s = []

  for i in range(n):
    for j in range(n):
      if l[i][j] == "s":
        s = [i, j]

  mn = 111111111111111
  ans = []
  for i in range(n):
    for j in range(n):
      if l[i][j] != 'p':
        continue
      d = dis(s, [i, j])

      if d < mn:
        mn = d
        ans = [s, [i, j]]

  p(f"({ans[0][0]},{ans[0][1]}):({ans[1][0]},{ans[1][1]}):{sqrt(mn):.2f}")

if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()