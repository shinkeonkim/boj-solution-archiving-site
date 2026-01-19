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

def dup(a, b):
  dis = (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

  return dis <= (a[2] + b[2]) ** 2

def solve():
  n = ii()

  circles = [mii() for _ in range(n)]

  cnt = [0] * n

  for i in range(n):
    for j in range(i + 1, n):
      if dup(circles[i], circles[j]):
        cnt[i] += 1
        cnt[j] += 1

  p(*cnt, sep="\n")

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()