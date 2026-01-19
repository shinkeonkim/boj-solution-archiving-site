import sys
from math import sqrt, pi, sin, cos, factorial, ceil, floor
from datetime import datetime, timedelta
# sys.setrecursionlimit(10**7)

BLANK = " "

# inp = input
inp = lambda : sys.stdin.readline().rstrip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
prt = print
def gcd(a, b): return gcd(b, a % b) if b > 0 else a
def lcm(a, b): return a * b // gcd(a, b)


def solve():
  a, b = inp().split()

  same = 0
  similar = 0

  chk_a = []
  chk_b = []

  for i in range(4):
    if a[i] == b[i]:
      same += 1
    else:
      chk_a.append(a[i])
      chk_b.append(b[i])
  
  chk_a.sort()
  chk_b.sort()

  i = j = 0

  while i < len(chk_a) and j < len(chk_b):
    if chk_a[i] == chk_b[j]:
      similar += 1
      i += 1
      j += 1
    elif chk_a[i] < chk_b[j]:
      i += 1
    else:
      j += 1
  
  prt(f"For secret = {a} and guess = {b}, {same} circles and {similar} squares will light up.")


if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()

