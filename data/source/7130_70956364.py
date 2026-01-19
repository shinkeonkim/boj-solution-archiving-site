import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  m, h = mii() # 우유 단위당 행복, 꿀 단위당 행복
  n = ii()
  l = [mii() for _ in range(n)]
  
  ans = 0
  
  for a, b in l:
    ans += max(a * m, b * h)
  
  p(ans)


if __name__ == "__main__":
  tc = 1
  
  for t in range(1, tc+1):
    solve()
