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

  d = {}  
  ans = 0

  for i in l:
    if i < 0:
      k = d.get(-i, 0)

      if k == 0:
        ans += 1

      d[-i] = 0
    else:
      d[i] = 1
  return ans

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
    p(ret)