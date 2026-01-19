import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def solve():
  ret = 0
  mx, n = mii()
  crt = 0

  for _ in range(n):
    s, a = input().split()
    a = int(a)

    if s == "leave":
      crt -= a
      continue

    if crt + a <= mx:
      crt += a
    else:
      ret += 1
  return ret

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
    p(ret)