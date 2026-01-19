import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  n, v = mii()
  ad = [mii() for _ in range(n)]
  c = [mii() for _ in range(v)]
  ans = 0

  for x, y, status in c:
    x -= 1
    y -= 1
    
    if ad[x][0] == 1:
      ans += ad[x][1]
    if ad[y][0] == 1:
      ans += ad[y][1]

    if status > 0:
      idx = [x, y][status - 1]
      if ad[idx][0] == 0:
        ans += ad[idx][1]

  return ans

  
if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()
    p(f"Data Set {t}:")
    p(ret)
    p()
