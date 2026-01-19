import sys
from math import sqrt, pi, sin, factorial

BLANK = " "

inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  n, *hate = mii()
  
  m = ii()
  
  cnt = 0
  for _ in range(m):
    k, *l = mii()
    for i in l:
      if i in hate:
        break
    else:
      cnt += 1
  print(cnt)

  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()

