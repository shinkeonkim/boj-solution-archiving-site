import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def solve():
  n, q = mii()
  l = [0] + [ii() for _ in range(n)]

  d = [0]

  for i in range(1, n + 1):
    d.append(d[i - 1] + l[i])

  for _ in range(q):
    a, b = mii()
    print(d[b] - d[a - 1])
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()