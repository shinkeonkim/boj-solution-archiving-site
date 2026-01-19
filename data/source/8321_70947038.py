import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  n, k, s = mii()
  l = sorted(mii(), reverse=True)
  
  o = k * s
  cnt = 0
  s = 0
  
  while s < o:
    s += l[cnt]
    cnt += 1
  print(cnt)
  
if __name__ == "__main__":
  tc = 1
  
  for t in range(1, tc+1):
    solve()
