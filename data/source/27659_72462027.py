import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def solve():
  input()

  n, e = mii()
  l = [ii() for _ in range(e)]

  d = {}

  for i in range(1, n + 1):
    d[i] = i

  k = 0

  for i in l:
    d[i] = k
    k -= 1

  return sorted(d.items(), key = lambda t : (-t[1]))[0][0]

if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()

    p(ret)