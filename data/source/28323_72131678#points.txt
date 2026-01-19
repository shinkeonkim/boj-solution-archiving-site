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
  l = mii()

  l = [i % 2 for i in l]
  
  cnt = 1

  for i in range(1, n):
    if l[i] == l[i - 1]:
      continue
    cnt += 1
  p(cnt)

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
