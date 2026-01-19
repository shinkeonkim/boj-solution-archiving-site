import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta
sys.setrecursionlimit(10**7)

BLANK = " "

# inp = input
inp = lambda : sys.stdin.readline().rstrip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def solve():
  n, m = mii()

  total = {}
  start = {}

  for i in range(m):
    num, category, h, m = input().split()

    num = int(num)
    h = int(h)
    m = int(m)

    tm = h * 60 + m

    if category == 'START':
      start[num] = tm
    else:
      total[num] = total.get(num, 0) + tm - start[num]

  for i in range(1, n + 1):
    tm = total.get(i, 0)

    p(f"{tm // 60} {tm % 60}")

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()