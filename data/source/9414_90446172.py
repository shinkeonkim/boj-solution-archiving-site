import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta

SYS_INPUT = True
RECURSION_LIMIT = 10 ** 7
SET_RECURSION = False
BLANK = " "

if SET_RECURSION:
  sys.setrecursionlimit(RECURSION_LIMIT)

inp = lambda : sys.stdin.readline().rstrip() if SYS_INPUT else input()
mii = lambda : [*map(int,inp().split())]
mfi = lambda : [*map(float,inp().split())]
ii = lambda : int(inp())
fi = lambda : float(inp())
isplit = lambda : inp().split()
p = print

def gcd(a, b): return gcd(b, a % b) if b > 0 else a
def lcm(a, b): return a * b // gcd(a, b)


def solve():
  l = []

  while 1:
    n = ii()
    if n == 0:
      break
    l.append(n)
  
  l.sort(reverse=True)
  ans = 0

  for idx, i in enumerate(l):
    ans += i ** (idx + 1)

    if ans > 2500000:
      break
  
  ans *= 2

  if ans <= 5000000:
    print(ans)
  else:
    print("Too expensive")

if __name__ == "__main__":
  tc = ii()
  for t in range(1, tc+1):
    ret = solve()