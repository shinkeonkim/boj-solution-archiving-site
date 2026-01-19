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
  k = []
  
  for i in range(1, n):
    k.append(l[i] - l[i - 1])
  
  mx = 1
  crt = k[0]
  cnt = 1
  
  for i in range(1, n - 1):
    if crt == k[i]:
      cnt += 1
    else:
      crt = k[i]
      cnt = 1
    mx = max(mx, cnt)
  return mx + 1
  
  
if __name__ == "__main__":
  tc = ii()
  
  for t in range(1, tc+1):
    d = solve()
    p(f"Case #{t}: {d}")
