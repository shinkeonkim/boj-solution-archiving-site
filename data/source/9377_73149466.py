import sys
from math import sqrt, pi, sin, factorial, ceil, floor

BLANK = " "

inp = input
# inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def solve():
  while 1:
    n = ii()

    if n == 0:
      break

    l = [input() for _ in range(n)]

    cnt = -1
    for _ in range(100):
      if "" in l:
        break
      if len(set(l)) < n:
        break

      l = [i[1:] for i in l]
      cnt += 1

    p(cnt)

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()