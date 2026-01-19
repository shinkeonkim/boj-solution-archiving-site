import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta
# sys.setrecursionlimit(10**7)

BLANK = " "

# inp = input
inp = lambda : sys.stdin.readline().rstrip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def solve():
  while 1:
    n, m = mii()

    if n == m == 0:
      break

    l = [0] * (m + 1)

    for i in range(n):
      floor, msg = input().split()

      l[int(floor)] = 1 if msg == "SAFE" else - 1

    last_safe = 1
    last_broken = m
    for i in range(1, m+1):
      if l[i] == 1:
        last_safe = i

    for i in range(m, 0, -1):
      if l[i] == -1:
        last_broken = i

    p(last_safe + 1, last_broken - 1)

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()