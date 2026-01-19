import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def solve():
  n = ii()
  x = ii()
  l = []
  ans = 0

  for i in range(n):
    l = mii()
    diff = abs(l[0] - l[1])

    if diff > x:
      a = ii()
      ans += a
    else:
      ans += max(l)

  return ans

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
    p(ret)
