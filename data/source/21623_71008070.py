import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  n, k = mii()
  l = mii()
  
  cnt = 0
  crt = k
  
  for i in l:
    if crt == 0:
      crt = k
    if crt - i >= 0:
      crt -= i

    if crt == 0:
      cnt += 1

  p(cnt)
  p(crt)
  
if __name__ == "__main__":
  tc = 1
  
  for t in range(1, tc+1):
    d = solve()
